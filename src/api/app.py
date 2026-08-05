"""FastAPI application for Smart Tourism Chatbot."""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from chatbot.service import get_chat_service  # noqa: E402
from config.settings import settings  # noqa: E402
from src.api.auth import require_api_key  # noqa: E402

logging.basicConfig(
    level=getattr(logging, settings.log_level.upper(), logging.INFO),
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)

app = FastAPI(
    title="Smart Tourism Chatbot API",
    description=(
        "Applied AI portfolio service: RAG-style tourism knowledge retrieval, "
        "intent routing, conversation logging, optional API-key auth."
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


class HistoryItem(BaseModel):
    user_message: str
    intent: str
    bot_response: str
    created_at: str


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
        "history": "GET /history",
    }
