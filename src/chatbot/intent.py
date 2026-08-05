"""
Intent recognition module (placeholder)
Will handle classification of user tourism-related intents.
"""

def detect_intent(user_message: str) -> str:
    """
    Basic placeholder for intent detection.
    Returns a simple intent label based on keywords.
    """
    message = user_message.lower()

    if any(word in message for word in ["hotel", "stay", "accommodation"]):
        return "hotel_query"
    elif any(word in message for word in ["place", "visit", "attraction", "tourist"]):
        return "attraction_query"
    elif any(word in message for word in ["plan", "itinerary", "trip"]):
        return "itinerary_query"
    else:
        return "general_query"
