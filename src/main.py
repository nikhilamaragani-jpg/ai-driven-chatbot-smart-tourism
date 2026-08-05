"""
Smart Tourism Chatbot — CLI entrypoint.

Uses the same ChatService as the FastAPI layer for consistent behaviour.
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from chatbot.service import get_chat_service  # noqa: E402
from config.settings import settings  # noqa: E402

logging.basicConfig(
    level=getattr(logging, settings.log_level.upper(), logging.INFO),
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)


def print_banner() -> None:
    print("=" * 60)
    print("  Smart Tourism Chatbot  |  Applied AI Portfolio Demo")
    print("  RAG-style retrieval · Intent routing · SQLite logging")
    print("  Commands: history | help | exit")
    print("=" * 60)
    print()


def print_help() -> None:
    print(
        "\nBot: Try questions like:\n"
        "  - best hotels in Paris\n"
        "  - places to visit / museum ideas\n"
        "  - visa requirements / how to reach\n"
        "  - local transport / metro tips\n"
        "  - budget planning / packing list\n"
        "  - itinerary for 3 days\n"
        "Commands: history | help | exit\n"
        "API: uvicorn src.api.app:app --reload\n"
    )


def main() -> None:
    service = get_chat_service()
    print_banner()

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Session ended.")
            break

        if user_input.lower() in {"exit", "quit", "bye"}:
            print("Bot: Thank you! Have a great trip.")
            break

        if user_input.lower() == "help":
            print_help()
            continue

        if user_input.lower() == "history":
            rows = service.history(5)
            if not rows:
                print("Bot: No conversation history yet.\n")
            else:
                print("\n--- Recent Conversations ---")
                for user_msg, intent, bot_msg, created_at in reversed(rows):
                    print(f"[{created_at}] Intent: {intent}")
                    print(f"  You: {user_msg}")
                    print(f"  Bot: {bot_msg}\n")
            continue

        if not user_input:
            continue

        result = service.chat(user_input)
        print(f"Bot ({result.intent}|{result.source}): {result.reply}\n")


if __name__ == "__main__":
    main()
