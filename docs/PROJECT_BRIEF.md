# Project brief — Smart Tourism Chatbot

| Field | Detail |
|-------|--------|
| Type | B.Tech **Major Project** (2025–2026) |
| Author | Amaragani Nikhil Sai (**22X31A0513**) |
| Institution | SIIET (JNTUH) |
| Guide | Ms. K. Mounika |
| Full report title | AI-Driven Chatbot Framework for Smart Tourism: A System Architecture and Systematic Review |
| Stack (this repo) | Python, FastAPI, scikit-learn (TF-IDF/hashing retrieval), SQLite, Docker |

## Goal

Design and demonstrate an AI-oriented tourism chatbot framework aligned with smart-tourism needs (including the **6A** view of tourism services), and ship a **runnable modular prototype** for intent handling, knowledge retrieval, response generation, and conversation logging.

## Prototype vs report

- **This repo:** CLI + FastAPI, local RAG-style retrieval, intent fallback, SQLite history, tests, Docker.  
- **Report:** literature/system analysis, UML, web UI vision, broader NLP/API/booking integrations.  

Keep claims aligned with what `python src/main.py` and `uvicorn src.api.app:app` actually run. See [REPORT_SUMMARY.md](REPORT_SUMMARY.md).
