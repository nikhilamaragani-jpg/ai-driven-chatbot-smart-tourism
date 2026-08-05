"""Application configuration via environment variables."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")


class Settings:
    app_name: str = os.getenv("APP_NAME", "smart-tourism-chatbot")
    app_env: str = os.getenv("APP_ENV", "development")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))
    db_path: str = os.getenv("DB_PATH", str(ROOT / "data" / "chat_history.db"))
    retriever_top_k: int = int(os.getenv("RETRIEVER_TOP_K", "3"))
    # Optional API key auth for /chat and /history (empty = disabled for local demos)
    api_key: str = os.getenv("API_KEY", "")
    # GenAI upgrade path (not required for local TF-IDF demo)
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    llm_provider: str = os.getenv("LLM_PROVIDER", "none")  # none | openai | stub


settings = Settings()
