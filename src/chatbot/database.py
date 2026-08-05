"""SQLite persistence for conversation history."""

from __future__ import annotations

import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

try:
    from config.settings import settings

    DB_PATH = settings.db_path
except Exception:  # pragma: no cover - fallback for simple imports
    BASE_DIR = Path(__file__).resolve().parents[2]
    DB_PATH = str(BASE_DIR / "data" / "chat_history.db")


def init_db() -> None:
    os.makedirs(os.path.dirname(DB_PATH) or ".", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_message TEXT NOT NULL,
                detected_intent TEXT,
                bot_response TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.commit()
    finally:
        conn.close()


def save_message(user_message: str, intent: str, bot_response: str) -> None:
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO conversations (user_message, detected_intent, bot_response, created_at) VALUES (?, ?, ?, ?)",
            (user_message, intent, bot_response, datetime.now(timezone.utc).isoformat()),
        )
        conn.commit()
    finally:
        conn.close()


def get_recent_messages(limit: int = 5):
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT user_message, detected_intent, bot_response, created_at FROM conversations ORDER BY id DESC LIMIT ?",
            (limit,),
        )
        return cursor.fetchall()
    finally:
        conn.close()
