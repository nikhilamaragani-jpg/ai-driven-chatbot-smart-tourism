"""
Intent recognition module for Smart Tourism Chatbot
"""

INTENT_KEYWORDS = {
    "hotel_query": ["hotel", "stay", "accommodation", "room", "lodge", "resort"],
    "attraction_query": ["place", "visit", "attraction", "tourist", "monument", "museum", "park"],
    "itinerary_query": ["plan", "itinerary", "trip", "schedule", "days", "tour"],
    "food_query": ["food", "restaurant", "eat", "cuisine", "cafe", "dinner", "lunch"],
    "transport_query": ["transport", "bus", "train", "flight", "taxi", "metro", "travel"],
    "budget_query": ["budget", "cost", "price", "cheap", "expensive", "affordable"],
    "greeting": ["hi", "hello", "hey", "good morning", "good evening"],
}


def detect_intent(user_message: str) -> str:
    """
    Detects user intent using keyword matching.
    Returns a label such as hotel_query, attraction_query, etc.
    """
    message = user_message.lower().strip()

    for intent, keywords in INTENT_KEYWORDS.items():
        if any(keyword in message for keyword in keywords):
            return intent

    return "general_query"
