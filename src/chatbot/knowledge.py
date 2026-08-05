"""
Simple tourism knowledge base for FAQ-style answers
"""

KNOWLEDGE_BASE = {
    "visa": "Visa requirements depend on your nationality and destination. Always check the official embassy or immigration website before travel.",
    "best time": "The best time to visit depends on the destination. Many popular cities are pleasant in spring and autumn due to milder weather.",
    "budget": "A simple daily budget often includes stay, food, local transport, and attractions. Tracking these four categories helps control costs.",
    "safety": "Use official transport options, keep digital copies of documents, and avoid sharing sensitive details with unknown contacts.",
    "packing": "Carry essentials: ID documents, medicines, chargers, comfortable shoes, and weather-appropriate clothing.",
    "local transport": "Public transport such as metro, buses, and official taxis is usually cost-effective for city travel.",
}


def search_knowledge(user_message: str) -> str | None:
    message = user_message.lower()
    for key, answer in KNOWLEDGE_BASE.items():
        if key in message:
            return answer
    return None
