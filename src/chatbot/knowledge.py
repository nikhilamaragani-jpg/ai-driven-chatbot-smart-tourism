"""
Tourism knowledge base aligned to smart-tourism / 6A assistance themes.

6A framework (report): Attractions, Accessibility, Amenities, Activities,
Available Packages, Ancillary Services.
"""

from typing import Optional

KNOWLEDGE_BASE = {
    # Attractions
    "attraction": (
        "Popular attractions usually include landmarks, museums, parks, and cultural sites. "
        "Share a city name for more targeted suggestions."
    ),
    "places to visit": (
        "Tell me the city or region you plan to visit and whether you prefer culture, nature, "
        "shopping, or nightlife. I can outline high-value places to prioritize."
    ),
    "museum": (
        "Museums often publish opening hours and ticket prices on official sites. "
        "Book timed-entry tickets for peak seasons when possible."
    ),
    # Accessibility / transport
    "visa": (
        "Visa requirements depend on your nationality and destination. "
        "Always verify with the official embassy/immigration website before travel."
    ),
    "how to reach": (
        "Common ways to reach a destination: flight + airport transfer, train, or intercity bus. "
        "Share origin/destination cities for a clearer route outline."
    ),
    "airport": (
        "For airports: arrive early, keep digital + printed boarding passes, and use official taxis "
        "or authorized rideshare zones."
    ),
    "local transport": (
        "Metro, city buses, and official taxis are usually cost-effective for urban travel. "
        "Day passes can reduce costs if you move frequently."
    ),
    "metro": (
        "Metro systems are often the fastest city option during peak traffic. "
        "Check multi-ride or tourist cards for savings."
    ),
    # Amenities
    "hotel": (
        "When choosing hotels, compare location, cancellation policy, breakfast inclusion, and reviews. "
        "Share destination + budget for better guidance."
    ),
    "stay": (
        "Stay options include hotels, hostels, and serviced apartments. "
        "Prioritize safety, commute time to attractions, and free cancellation when unsure."
    ),
    # Activities / packages
    "itinerary": (
        "A simple itinerary structure: Day 1 orientation + key landmark, Day 2 cultural sites, "
        "Day 3 neighborhood food walk. Share trip length for a tighter plan."
    ),
    "package": (
        "Travel packages may bundle stay + transport + activities. "
        "Compare inclusions carefully (meals, transfers, entry tickets)."
    ),
    "activity": (
        "Activities range from guided tours to outdoor experiences. "
        "Match activities to weather, energy level, and daily budget."
    ),
    # Ancillary / practical
    "best time": (
        "Best time to visit depends on climate and crowd patterns. "
        "Shoulder seasons (spring/autumn) often balance weather and price."
    ),
    "budget": (
        "Track four daily categories: stay, food, local transport, and attractions. "
        "This keeps trip costs predictable."
    ),
    "safety": (
        "Use official transport, keep digital copies of documents, avoid oversharing personal data, "
        "and store emergency contacts offline."
    ),
    "packing": (
        "Essentials: ID/passport, medicines, chargers, comfortable shoes, and weather-ready clothing. "
        "Add a power bank for navigation-heavy days."
    ),
    "emergency": (
        "Save local emergency numbers, your embassy contact, and hotel address offline. "
        "Share your daily plan with a trusted contact when traveling alone."
    ),
    "food": (
        "For food, balance local specialties with hygiene-safe choices. "
        "Ask for popular local dishes and allergy-friendly options when ordering."
    ),
    "currency": (
        "Prefer official exchange counters or ATMs with transparent fees. "
        "Notify your bank before international travel to avoid card blocks."
    ),
}


def search_knowledge(user_message: str) -> Optional[str]:
    message = user_message.lower()
    # Longer keys first for better matching
    for key in sorted(KNOWLEDGE_BASE.keys(), key=len, reverse=True):
        if key in message:
            return KNOWLEDGE_BASE[key]
    return None
