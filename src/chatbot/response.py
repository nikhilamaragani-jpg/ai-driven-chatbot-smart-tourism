"""
Response generation module for Smart Tourism Chatbot
"""

RESPONSES = {
    "hotel_query": (
        "I can help with hotel suggestions. "
        "Please share your destination, travel dates, and preferred budget range."
    ),
    "attraction_query": (
        "Looking for places to visit? Tell me the city or region, "
        "and I can suggest popular attractions and experiences."
    ),
    "itinerary_query": (
        "I can help you plan an itinerary. "
        "How many days will you travel, and which city are you visiting?"
    ),
    "food_query": (
        "Great choice! Share the city and cuisine preference "
        "(local, vegetarian, fine dining, street food), and I can guide you."
    ),
    "transport_query": (
        "I can help with transport options. "
        "Are you looking for local commute, intercity travel, or airport transfers?"
    ),
    "budget_query": (
        "Budget planning is important. "
        "Share your destination and approximate budget, and I can suggest cost-friendly options."
    ),
    "greeting": (
        "Hello! I am your Smart Tourism assistant. "
        "I can help with hotels, attractions, food, transport, and itinerary planning."
    ),
    "general_query": (
        "I am a tourism assistant chatbot. "
        "You can ask me about hotels, places to visit, food, transport, or trip planning."
    ),
}


def generate_response(intent: str) -> str:
    """
    Returns a response based on the detected intent.
    """
    return RESPONSES.get(intent, RESPONSES["general_query"])
