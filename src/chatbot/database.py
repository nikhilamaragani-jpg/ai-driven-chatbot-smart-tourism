"""SQLite persistence for conversation history."""

from __future__ import annotations

import os
import sqlite3
from datetime import datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List

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
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_conversations_created_at ON conversations(created_at)"
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS conversation_feedback (
                conversation_id INTEGER PRIMARY KEY,
                rating TEXT NOT NULL CHECK (rating IN ('helpful', 'not_helpful')),
                created_at TEXT NOT NULL,
                FOREIGN KEY (conversation_id) REFERENCES conversations(id)
            )
            """
        )
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_feedback_created_at ON conversation_feedback(created_at)"
        )
        conn.commit()
    finally:
        conn.close()


def save_message(user_message: str, intent: str, bot_response: str) -> int:
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO conversations (user_message, detected_intent, bot_response, created_at) VALUES (?, ?, ?, ?)",
            (user_message, intent, bot_response, datetime.now(timezone.utc).isoformat()),
        )
        conn.commit()
        return int(cursor.lastrowid)
    finally:
        conn.close()


def save_feedback(conversation_id: int, rating: str) -> bool:
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT 1 FROM conversations WHERE id = ?", (conversation_id,)
        )
        if cursor.fetchone() is None:
            return False

        cursor.execute(
            """
            INSERT INTO conversation_feedback (conversation_id, rating, created_at)
            VALUES (?, ?, ?)
            ON CONFLICT(conversation_id) DO UPDATE SET
                rating = excluded.rating,
                created_at = excluded.created_at
            """,
            (conversation_id, rating, datetime.now(timezone.utc).isoformat()),
        )
        conn.commit()
        return True
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


def get_analytics(days: int = 30) -> Dict[str, Any]:
    today = datetime.now(timezone.utc).date()
    start_date = today - timedelta(days=days - 1)
    start_at = datetime.combine(start_date, time.min, tzinfo=timezone.utc).isoformat()
    daily_counts: Dict[str, int] = {}

    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT substr(created_at, 1, 10), COUNT(*)
            FROM conversations
            WHERE created_at >= ?
            GROUP BY substr(created_at, 1, 10)
            """,
            (start_at,),
        )
        daily_counts = {day: count for day, count in cursor.fetchall()}

        cursor.execute(
            """
            SELECT
                CASE
                    WHEN instr(COALESCE(detected_intent, ''), '|') > 0
                    THEN substr(detected_intent, 1, instr(detected_intent, '|') - 1)
                    ELSE COALESCE(NULLIF(detected_intent, ''), 'unknown')
                END AS intent,
                COUNT(*)
            FROM conversations
            WHERE created_at >= ?
            GROUP BY intent
            ORDER BY COUNT(*) DESC, intent
            """,
            (start_at,),
        )
        intent_counts = [
            {"name": name, "count": count} for name, count in cursor.fetchall()
        ]

        cursor.execute(
            """
            SELECT
                CASE
                    WHEN instr(COALESCE(detected_intent, ''), '|') > 0
                    THEN substr(detected_intent, instr(detected_intent, '|') + 1)
                    ELSE 'unknown'
                END AS source,
                COUNT(*)
            FROM conversations
            WHERE created_at >= ?
            GROUP BY source
            ORDER BY COUNT(*) DESC, source
            """,
            (start_at,),
        )
        source_counts = [
            {"name": name, "count": count} for name, count in cursor.fetchall()
        ]

        cursor.execute(
            """
            SELECT rating, COUNT(*)
            FROM conversation_feedback
            WHERE created_at >= ?
            GROUP BY rating
            ORDER BY rating
            """,
            (start_at,),
        )
        feedback_counts = [
            {"name": name, "count": count} for name, count in cursor.fetchall()
        ]
    finally:
        conn.close()

    feedback_total = sum(item["count"] for item in feedback_counts)
    helpful_count = sum(
        item["count"] for item in feedback_counts if item["name"] == "helpful"
    )
    daily_volume: List[Dict[str, Any]] = []
    for offset in range(days):
        day = start_date + timedelta(days=offset)
        day_text = day.isoformat()
        daily_volume.append(
            {"date": day_text, "count": daily_counts.get(day_text, 0)}
        )

    return {
        "days": days,
        "total_chat_turns": sum(item["count"] for item in daily_volume),
        "daily_volume": daily_volume,
        "intent_counts": intent_counts,
        "source_counts": source_counts,
        "feedback_total": feedback_total,
        "helpful_rate_pct": (
            round(helpful_count / feedback_total * 100, 1)
            if feedback_total
            else None
        ),
        "feedback_counts": feedback_counts,
    }
