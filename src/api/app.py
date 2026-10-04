"""FastAPI application for Smart Tourism Chatbot."""

from __future__ import annotations

import csv
import io
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.responses import Response
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from chatbot.service import get_chat_service  # noqa: E402
from config.settings import settings  # noqa: E402

try:
    from .auth import require_api_key
except ImportError:  # pragma: no cover
    from src.api.auth import require_api_key  # type: ignore

logging.basicConfig(
    level=getattr(logging, settings.log_level.upper(), logging.INFO),
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)

app = FastAPI(
    title="Smart Tourism Chatbot API",
    description=(
        "Applied AI portfolio service: RAG-style tourism knowledge retrieval, "
        "intent routing, conversation logging, usage analytics, optional API-key auth."
    ),
    version="0.3.0",
)


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000, examples=["places to visit in Paris"])


class ChatResponse(BaseModel):
    reply: str
    intent: str
    source: str
    retrieval_scores: List[Dict[str, Any]]
    conversation_id: Optional[int] = None


class HistoryItem(BaseModel):
    user_message: str
    intent: str
    bot_response: str
    created_at: str


class AnalyticsCount(BaseModel):
    name: str
    count: int


class DailyVolume(BaseModel):
    date: str
    count: int


class AnalyticsResponse(BaseModel):
    days: int
    total_chat_turns: int
    daily_volume: List[DailyVolume]
    intent_counts: List[AnalyticsCount]
    source_counts: List[AnalyticsCount]
    feedback_total: int
    helpful_rate_pct: Optional[float]
    feedback_counts: List[AnalyticsCount]


class FeedbackRequest(BaseModel):
    conversation_id: int = Field(..., gt=0)
    rating: Literal["helpful", "not_helpful"]


class FeedbackResponse(BaseModel):
    conversation_id: int
    rating: Literal["helpful", "not_helpful"]


@app.get("/health")
def health() -> Dict[str, str]:
    return {
        "status": "ok",
        "app": settings.app_name,
        "env": settings.app_env,
        "auth": "enabled" if settings.api_key else "disabled",
        "llm_provider": settings.llm_provider,
    }


@app.post("/chat", response_model=ChatResponse, dependencies=[Depends(require_api_key)])
def chat(payload: ChatRequest) -> ChatResponse:
    try:
        result = get_chat_service().chat(payload.message)
        return ChatResponse(**result.to_dict())
    except Exception as exc:  # pragma: no cover
        logging.exception("chat_failed")
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post(
    "/feedback",
    response_model=FeedbackResponse,
    dependencies=[Depends(require_api_key)],
)
def feedback(payload: FeedbackRequest) -> FeedbackResponse:
    if not get_chat_service().feedback(payload.conversation_id, payload.rating):
        raise HTTPException(status_code=404, detail="Conversation not found.")
    return FeedbackResponse(
        conversation_id=payload.conversation_id,
        rating=payload.rating,
    )


@app.get(
    "/analytics",
    response_model=AnalyticsResponse,
    dependencies=[Depends(require_api_key)],
)
def analytics(days: int = Query(default=30, ge=1, le=365)) -> AnalyticsResponse:
    return AnalyticsResponse(**get_chat_service().analytics(days))


@app.get("/analytics/export.csv", dependencies=[Depends(require_api_key)])
def analytics_csv(days: int = Query(default=30, ge=1, le=365)) -> Response:
    summary = get_chat_service().analytics(days)
    output = io.StringIO(newline="")
    writer = csv.writer(output)
    writer.writerow(["date", "metric", "dimension", "value"])
    for item in summary["daily_volume"]:
        writer.writerow([item["date"], "chat_turns", "", item["count"]])
    for metric in ("intent_counts", "source_counts"):
        metric_name = metric.removesuffix("_counts")
        for item in summary[metric]:
            writer.writerow(["", metric_name, item["name"], item["count"]])
    for item in summary["feedback_counts"]:
        writer.writerow(["", "feedback", item["name"], item["count"]])
    helpful_rate = summary["helpful_rate_pct"]
    writer.writerow(
        ["", "feedback", "helpful_rate_pct", helpful_rate if helpful_rate is not None else ""]
    )
    return Response(
        content=output.getvalue(),
        media_type="text/csv",
        headers={
            "Content-Disposition": 'attachment; filename="tourism-analytics.csv"'
        },
    )


@app.get("/history", response_model=List[HistoryItem], dependencies=[Depends(require_api_key)])
def history(limit: int = 5) -> List[HistoryItem]:
    limit = max(1, min(limit, 50))
    rows = get_chat_service().history(limit)
    items: List[HistoryItem] = []
    for user_msg, intent, bot_msg, created_at in rows:
        items.append(
            HistoryItem(
                user_message=user_msg,
                intent=intent or "",
                bot_response=bot_msg,
                created_at=created_at,
            )
        )
    return items


@app.get("/")
def root() -> Dict[str, Optional[str]]:
    return {
        "service": settings.app_name,
        "version": "0.3.0",
        "docs": "/docs",
        "health": "/health",
        "chat": "POST /chat",
        "feedback": "POST /feedback",
        "analytics": "GET /analytics",
        "history": "GET /history",
    }
