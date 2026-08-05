# Architecture

## Goals

- Demonstrate Applied AI service design for junior ML / AI engineering interviews.
- Keep the local demo free of paid API keys.
- Make retrieval and generation swappable.

## Components

| Component | Responsibility |
|-----------|----------------|
| `retriever.py` | TF-IDF index + top-k knowledge retrieval (RAG-style) |
| `intent.py` | Lightweight intent labels for analytics / fallback |
| `response.py` | Template replies when retrieval is weak |
| `service.py` | Orchestration + logging |
| `database.py` | SQLite conversation store |
| `api/app.py` | REST surface (health, chat, history) |

## Data flow

1. Query enters via CLI or `POST /chat`.
2. Retriever scores FAQ corpus.
3. If score ≥ threshold → grounded answer.
4. Else → intent template.
5. Persist turn for evaluation / demos.

## Upgrade path (not claimed implemented)

- Replace TF-IDF with embeddings + Chroma/FAISS/pgvector.
- Add LangChain chains for tool use.
- Call LLM APIs only for generation, keep retrieval grounded.
- Add auth middleware and rate limits.
