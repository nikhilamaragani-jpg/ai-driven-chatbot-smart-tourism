# Project walkthrough — Smart Tourism Chatbot (from major report + repo)

## 60-second pitch

My major project is *AI-Driven Chatbot Framework for Smart Tourism* (guide: Ms. K. Mounika, SIIET / JNTUH, 2025–26, roll 22X31A0513). The report studies chatbot architecture for tourism and the **6A framework**. On GitHub I ship a modular runnable prototype: RAG-style retrieval over a tourism knowledge base, intent fallback, SQLite logging, and a FastAPI API — so the core pipeline can be demoed without paid APIs.

## Academic anchors (from report)

- **Problem:** rule-based bots, weak context, limited personalization and integrations.  
- **Objectives:** intelligent travel assistance, multi-turn style interaction, path to multilingual and service integration.  
- **Design layers:** UI → NLP/processing → AI/ML → database → integration → response.  

## What I demo from the repo

```bash
pip install -r requirements.txt
python src/main.py
# or: uvicorn src.api.app:app --reload
```

Try: `places to visit` · `budget planning` · `history` · `exit`  
API: `POST /chat` returns `intent`, `source`, `retrieval_scores`.

## Honest scope answers

**Is this the full report system?**  
No. Report includes systematic review, UML, and web/booking vision (sample Django/OpenAI-oriented snippets). Repo = focused prototype that runs offline.

**What is 6A?**  
Attractions, Accessibility, Amenities, Activities, Available Packages, Ancillary Services — used in the report to map chatbot value in tourism.

**Why TF-IDF first?**  
Deterministic demos, no API key required; architecture allows swapping embeddings/LLM later.
