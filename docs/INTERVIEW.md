# Project walkthrough — Smart Tourism Chatbot

## 60-second summary

Tourism needs structured assistance. My major project ships a modular Python prototype with RAG-style retrieval over a tourism knowledge base, intent fallbacks, SQLite conversation logging, and a FastAPI interface. The local demo runs without paid APIs so it is reliable to show.

## Architecture

1. User message (CLI or API)  
2. Knowledge retrieval (TF-IDF / hashing vectors)  
3. Intent fallback if retrieval is weak  
4. Save turn to SQLite  

## Demo

```bash
pip install -r requirements.txt
python src/main.py
# or: uvicorn src.api.app:app --reload
```

Try: `places to visit` · `budget planning` · `history` · `exit`

## Questions

**Why modular design?** Clear layers make stronger NLP or embeddings easier to add later.  
**Why local retrieval first?** Deterministic demos, no API cost, grounded FAQ answers.  
**Prototype vs report?** Repo = focused runnable core; report covers broader research and future integrations.
