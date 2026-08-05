"""
Optional LLM generation layer (GenAI upgrade path).

Default: no external LLM (retrieval + templates only).
When OPENAI_API_KEY + LLM_PROVIDER=openai are set, generation can be enabled.
LangChain orchestration is documented as an adapter target — not required offline.
"""

from __future__ import annotations

import logging
from typing import List, Optional

from config.settings import settings

logger = logging.getLogger(__name__)


def build_prompt(query: str, contexts: List[str]) -> str:
    """Simple prompt-engineering template for grounded tourism answers."""
    ctx = "\n".join(f"- {c}" for c in contexts) if contexts else "- (no context)"
    return (
        "You are a careful tourism assistant. Answer using ONLY the context. "
        "If context is insufficient, say what extra detail you need.\n\n"
        f"Context:\n{ctx}\n\nUser question: {query}\n\nAnswer:"
    )


def generate_with_llm(query: str, contexts: List[str]) -> Optional[str]:
    """
    Returns LLM text if configured; otherwise None (caller uses retrieval/templates).

    OpenAI path is optional and skipped when no key is present — no fake claims.
    """
    provider = (settings.llm_provider or "none").lower()
    if provider in {"", "none"}:
        return None

    if provider == "stub":
        prompt = build_prompt(query, contexts)
        logger.info("llm_stub_prompt_chars=%s", len(prompt))
        return (
            "[LLM stub] Grounded summary based on retrieved tourism context: "
            + (contexts[0] if contexts else "No context retrieved.")
        )

    if provider == "openai":
        if not settings.openai_api_key:
            logger.warning("LLM_PROVIDER=openai but OPENAI_API_KEY is empty")
            return None
        # TODO: implement official OpenAI SDK call when key is available.
        # Keeping explicit TODO avoids shipping broken paid-API code in demos.
        logger.warning("OpenAI generation not wired in this portfolio build — use stub or retrieval")
        return None

    logger.warning("Unknown LLM_PROVIDER=%s", provider)
    return None
