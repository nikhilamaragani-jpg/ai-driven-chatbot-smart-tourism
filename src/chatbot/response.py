"""
Response generation module (placeholder)
"""

def generate_response(intent: str) -> str:
    """
    Returns a simple response based on detected intent.
    """
    responses = {
        "hotel_query": "I can help you with hotel recommendations. Please share your destination and budget.",
        "attraction_query": "Looking for places to visit? Tell me the city you're interested in.",
        "itinerary_query": "I can help you plan an itinerary. How many days will you be traveling?",
        "general_query": "Hello! I am a tourism assistant chatbot. How can I help you today?"
    }
    return responses.get(intent, responses["general_query"])
