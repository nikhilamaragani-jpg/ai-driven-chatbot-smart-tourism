# Interview Guide — Smart Tourism Chatbot

Use this document when a recruiter or hiring manager asks you to walk through the project.

## 60-second pitch

> Tourism is information-heavy. Existing bots are often rule-only and lose context. My major project designs an AI-driven chatbot framework for smart tourism and ships a runnable modular prototype: intent detection, a tourism knowledge base, response generation, and SQLite conversation logging.

## Problem → Solution → Impact

| | |
|--|--|
| **Problem** | Rule-based tourism bots fail on multi-turn, personalization, and integration |
| **Solution** | Layered architecture (query → knowledge/AI → response → DB) |
| **Impact** | 24/7 assistance model, analytics via chat history, extensible to LLMs/APIs |

## Architecture (say this out loud)

1. User sends natural language
2. Knowledge FAQ match runs first (fast path)
3. Else intent classifier routes the query
4. Response module returns structured guidance
5. Interaction is logged for review/analytics

## Expected questions & strong answers

**Q: Why not just call ChatGPT?**  
A: Production systems still need domain knowledge, logging, guardrails, cost control, and integration with booking systems. This project shows that systems design, not only a single API call.

**Q: How would you add multilingual support?**  
A: Detect language → translate to English for intent → answer → translate back; or train multilingual intent classifiers.

**Q: How do you measure success?**  
A: Intent accuracy, containment rate (resolved without human), CSAT, booking conversion, and response latency.

**Q: What is the 6A framework?**  
A: Attractions, Accessibility, Amenities, Activities, Available Packages, Ancillary Services — used in the report to map chatbot value across tourism services.

## Demo script (3 minutes)

```bash
pip install -r requirements.txt
python src/main.py
```

Try:
1. `hello`
2. `places to visit`
3. `visa requirements`
4. `budget planning`
5. `history`
6. `exit`

## Resume bullets (copy-ready)

- Designed a modular **AI tourism chatbot** with intent routing, knowledge-base answers, and SQLite conversation history for analytics.
- Mapped chatbot capabilities to the **smart tourism 6A framework** and documented architecture, requirements, and future LLM/API integrations.
- Built a runnable CLI prototype recruiters can clone and evaluate in under 5 minutes.
