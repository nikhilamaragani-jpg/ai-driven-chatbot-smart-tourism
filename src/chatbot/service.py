"""Orchestration layer for chat turns."""

from __future__ import annotations

import logging
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional

from .database import get_recent_messages, init_db, save_message
from .intent import detect_intent
from .response import generate_response
from .retriever import get_retriever

logger = logging.getLogger(__name__)


@dataclass
class ChatResult:
    reply: str
    intent: str
    source: str  # retrieval | intent_template
    retrieval_scores: List[Dict[str, Any]]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class ChatService:
    def __init__(self, top_k: int = 3) -> None:
        self.top_k = top_k
        self.retriever = get_retriever()
        init_db()

    def chat(self, message: str, persist: bool = True) -> ChatResult:
        message = (message or "").strip()
        if not message:
            return ChatResult(
                reply="Please enter a tourism-related question.",
                intent="empty",
                source="intent_template",
                retrieval_scores=[],
            )

        answer, chunks = self.retriever.best_answer(message)
        intent = detect_intent(message)
        scores = [{"key": c.key, "score": round(c.score, 4)} for c in chunks[: self.top_k]]

        if answer:
            reply = answer
            source = "retrieval"
        else:
            reply = generate_response(intent)
            source = "intent_template"

        if persist:
            save_message(message, f"{intent}|{source}", reply)
            logger.info("chat_turn intent=%s source=%s", intent, source)

        return ChatResult(
            reply=reply,
            intent=intent,
            source=source,
            retrieval_scores=scores,
        )

    def history(self, limit: int = 5) -> List[tuple]:
        return get_recent_messages(limit)


_service: Optional[ChatService] = None


def get_chat_service() -> ChatService:
    global _service
    if _service is None:
        _service = ChatService()
    return _service
