"""
AI-Driven Chatbot Framework for Smart Tourism
Basic entry point - Academic Prototype
"""

from chatbot.intent import detect_intent
from chatbot.response import generate_response


def main():
    print("=" * 50)
    print("Smart Tourism Chatbot - Prototype")
    print("=" * 50)
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Thank you! Have a great trip!")
            break

        if not user_input:
            continue

        intent = detect_intent(user_input)
        reply = generate_response(intent)
        print(f"Bot: {reply}\n")


if __name__ == "__main__":
    main()
