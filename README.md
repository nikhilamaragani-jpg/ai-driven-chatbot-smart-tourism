<div align="center">

# Smart Tourism Chatbot

### Production-style Applied AI Service · RAG · FastAPI · Docker

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-REST-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](Dockerfile)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](.github/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Amaragani Nikhil Sai** · Portfolio flagship for Junior Applied AI / ML / Backend roles  
Runnable offline demo. Optional API-key auth. GenAI upgrades documented — not claimed as paid production traffic.

[Problem](#problem) · [Solution](#solution) · [Architecture](#architecture) · [Installation](#installation) · [Usage](#usage)

</div>

---

## Problem

Travel support systems need grounded answers (visas, transport, budgets, attractions). Pure keyword bots fail on paraphrases; LLM-only bots risk ungrounded replies and high cost without retrieval.

---

## Solution

A **production-style Applied AI service** with:

- RAG-style retrieval over a curated tourism knowledge base  
- Intent routing fallback  
- FastAPI REST API + CLI  
- Optional API-key authentication  
- SQLite conversation logging  
- Offline evaluation harness  
- Docker packaging + CI tests  
- Documented LangChain / vector DB / LLM upgrade path  

---

## Features

| Feature | Status |
|---------|--------|
| TF-IDF / hashing vector retrieval | Implemented |
| Intent + template fallback | Implemented |
| REST: health, chat, history | Implemented |
| Optional `X-API-Key` auth | Implemented |
| Evaluation script (hit-rate) | Implemented |
| Docker + GitHub Actions | Implemented |
| LangChain / Chroma / OpenAI | Scaffold + TODO (honest) |

---

## Architecture

![Architecture](images/architecture.svg)

![Workflow](images/workflow.svg)

```text
Client → FastAPI (+ optional API key)
            ├─ Retriever (RAG-style)
            ├─ Intent router
            └─ Composer / optional LLM
                    ↓
            SQLite conversation log
```

---

## Tech stack

Python · FastAPI · Pydantic · scikit-learn · NumPy · SQLite · Docker · pytest · GitHub Actions  
Keywords: NLP, RAG, GenAI design, REST API, Applied AI, logging, configuration

---

## Folder structure

```text
config/  src/api/  src/chatbot/  tests/  docs/  scripts/  images/  data/
Dockerfile  docker-compose.yml  requirements.txt  .github/workflows/ci.yml
```

---

## Installation

```bash
git clone https://github.com/nikhilamaragani-jpg/ai-driven-chatbot-smart-tourism.git
cd ai-driven-chatbot-smart-tourism
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

---

## Usage

```bash
# CLI
python src/main.py

# API
uvicorn src.api.app:app --reload --port 8000

# Evaluate retrieval
python scripts/evaluate_retrieval.py

# Tests
pytest -q

# Docker
docker compose up --build
```

```bash
curl -s http://127.0.0.1:8000/health
curl -s -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"budget planning tips"}'
```

With auth: set `API_KEY` and pass header `X-API-Key`.

---

## Project workflow

1. Curate tourism FAQ knowledge  
2. Index for retrieval  
3. Accept query via CLI/API  
4. Retrieve → compose (or intent template / optional LLM)  
5. Log turn → return structured JSON  
6. Evaluate hit-rate offline  

---

## Screenshots

| Asset | Path |
|-------|------|
| Architecture | [images/architecture.svg](images/architecture.svg) |
| Workflow | [images/workflow.svg](images/workflow.svg) |
| API docs | Run server → `/docs` (capture to `images/api_docs.png`) |
| Eval sample | [data/outputs/retrieval_eval.sample.json](data/outputs/retrieval_eval.sample.json) |

---

## Results

- Offline retrieval eval sample: hit-rate **1.0** on 6 labeled queries (re-run script for live numbers)  
- API returns `intent`, `source`, `retrieval_scores` for debugging and interviews  

---

## Future improvements

- [ ] Wire OpenAI / local LLM generation when key present  
- [ ] Chroma/FAISS embeddings backend  
- [ ] Full LangChain retrieval chain  
- [ ] PostgreSQL multi-user history  
- [ ] Cloud deploy (Render/Azure) with secrets  
- [ ] Agent tools (weather/maps) with strict grounding  

---

## Skills demonstrated

Applied AI · NLP · RAG design · REST APIs · authentication basics · evaluation · Docker · CI · modular Python · documentation for hiring reviews

---

## Documentation

[PROJECT_BRIEF](docs/PROJECT_BRIEF.md) · [DEMO](docs/DEMO.md) · [API](docs/API.md) · [ARCHITECTURE](docs/ARCHITECTURE.md) · [EVALUATION](docs/EVALUATION.md) · [DEPLOYMENT](docs/DEPLOYMENT.md) · [GENAI_ROADMAP](docs/GENAI_ROADMAP.md) · [INTERVIEW](docs/INTERVIEW.md) · [RESUME_BULLETS](docs/RESUME_BULLETS.md)

---

## License

MIT — see [LICENSE](LICENSE).

**Author:** Amaragani Nikhil Sai · https://nikhilamaragani-jpg.github.io/ · nikhilamaragani@gmail.com
