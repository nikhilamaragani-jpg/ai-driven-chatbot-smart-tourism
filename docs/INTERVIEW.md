# Interview walkthrough — Smart Tourism Chatbot

## 60-second pitch

I built a tourism Applied AI service with a retrieval layer over a curated knowledge base, intent fallbacks, SQLite conversation logging, and a FastAPI interface. Locally it runs without paid APIs using TF-IDF retrieval so demos are reliable. The architecture is designed so retrieval and generation can be upgraded independently.

## Design questions

**Why not only an LLM?**  
Grounding + cost control. Retrieval first reduces hallucination for FAQ-style tourism help.

**Why TF-IDF?**  
Deterministic, offline, easy to explain metrics. Production path: embeddings + vector DB.

**How would you evaluate?**  
Precision@k on FAQ labels, human groundedness checklist, latency, and logging of source path (retrieval vs template).

**What breaks first at scale?**  
SQLite write contention, single-process embedding load, lack of auth/rate limits — all roadmap items.

## Demo

CLI + `POST /chat` + show `retrieval_scores` in JSON.
