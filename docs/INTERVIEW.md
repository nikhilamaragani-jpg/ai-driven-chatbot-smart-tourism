# Project walkthrough — Smart Tourism Chatbot

## 60-second summary

Tourism needs fast, structured assistance. Many bots are rule-only and lose context. My major project proposes a layered chatbot framework and ships a modular Python prototype with intent routing, a tourism knowledge base, response generation, and SQLite conversation history.

## Architecture

1. User message  
2. Knowledge FAQ match (fast path) or intent detection  
3. Response generation  
4. Save turn to SQLite  

## Demo

```bash
pip install -r requirements.txt
python src/main.py
```

Try: `hello` → `places to visit` → `budget planning` → `history` → `exit`

## Questions

**Why modular design instead of one script?**  
Clear layers make it easier to replace intent logic with stronger NLP later.

**What is the 6A framework?**  
Attractions, Accessibility, Amenities, Activities, Available Packages, Ancillary Services — used in the report to map chatbot value.

**Prototype vs full report?**  
The repo is a focused prototype; the report covers broader research, diagrams, and future web/API integrations.
