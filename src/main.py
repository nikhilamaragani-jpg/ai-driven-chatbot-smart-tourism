"""
AI-Driven Chatbot Framework for Smart Tourism
Prototype with intent detection + knowledge base + SQLite history
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from chatbot.intent import detect_intent
from chatbot.response import generate_response
from chatbot.knowledge import search_knowledge
from chatbot.database import init_db, save_message, get_recent_messages


def main():
    init_db()

    print("=" * 55)
    print("Smart Tourism Chatbot - Prototype")
    print("Commands: 'history' to view recent chats | 'exit' to quit")
    print("=" * 55)
    print()

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Thank you! Have a great trip!")
            break

        if user_input.lower() == "history":
            rows = get_recent_messages(5)
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

        knowledge_answer = search_knowledge(user_input)
        if knowledge_answer:
            intent = "knowledge_faq"
            reply = knowledge_answer
        else:
            intent = detect_intent(user_input)
            reply = generate_response(intent)

        save_message(user_input, intent, reply)
        print(f"Bot ({intent}): {reply}\n")


if __name__ == "__main__":
    main()
