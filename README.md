<div align="center">

# AI-Driven Chatbot Framework for Smart Tourism

### B.Tech Major Project · Conversational AI · NLP concepts · System Architecture

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Runnable%20Prototype-success)](https://github.com/nikhilamaragani-jpg/ai-driven-chatbot-smart-tourism)

**Amaragani Nikhil Sai** · 22X31A0513 · SIIET (JNTUH) · Guide: Ms. K. Mounika · 2025–2026

[Quick start](#quick-start) · [Architecture](#system-architecture) · [Scope](#implementation-status) · [Docs](#documentation)

</div>

---

## Problem

Tourism support is information-heavy. Many bots rely on fixed scripts, lose multi-turn context, and give generic answers. This major project studies AI chatbots for smart tourism and ships a **runnable modular prototype** for intent handling, knowledge-base answers, and conversation logging.

| Gap | This project |
|-----|----------------|
| Rule-only keyword bots | Intent-based routing |
| No conversation memory | Multi-turn CLI + SQLite history |
| Generic answers | Tourism knowledge base (6A-aligned FAQs) |
| Weak structure for extension | Modular package layout |

---

## System architecture

```text
User (CLI)
    |
    v
Query processing  →  intent detection (keyword / rule NLP-style)
    |
    v
Knowledge + logic →  FAQ match · recommendations
    |
    v
Response generation → structured replies
    |
    v
Persistence (SQLite) → conversation history
```

---

## Tech stack

| Layer | Technology |
|-------|------------|
| Language | Python 3 |
| Design | Modular package `src/chatbot/` |
| Storage | SQLite |
| Interface | CLI demo |
| Report vision | Broader NLP engines, web UI, external APIs |

---

## Quick start

```bash
git clone https://github.com/nikhilamaragani-jpg/ai-driven-chatbot-smart-tourism.git
cd ai-driven-chatbot-smart-tourism
pip install -r requirements.txt
python src/main.py
```

**Try:** `hello` · `places to visit` · `visa requirements` · `budget planning` · `history` · `help` · `exit`

---

## Skills demonstrated

| Skill | Evidence |
|-------|----------|
| Problem decomposition | Tourism pain points → layered design |
| Conversational pipeline | Intent + knowledge + response modules |
| Software structure | Clear package boundaries, single entrypoint |
| Persistence | SQLite chat history |
| Documentation | Brief, demo, interview, resume bullets |

---

## Implementation status

**Runnable prototype (this repo)**
- [x] Intent routing  
- [x] Knowledge-base FAQs  
- [x] Response generation  
- [x] SQLite conversation logging  
- [x] Modular codebase  

**Full report scope / future work**
- [ ] Transformer / LLM backend  
- [ ] Multilingual support  
- [ ] Live booking / travel API integrations  
- [ ] Full web UI from report screens  

---

## Documentation

| File | Purpose |
|------|---------|
| [docs/PROJECT_BRIEF.md](docs/PROJECT_BRIEF.md) | Technical brief |
| [docs/DEMO.md](docs/DEMO.md) | Demo walkthrough |
| [docs/INTERVIEW.md](docs/INTERVIEW.md) | Pitch, Q&A, demo script |
| [docs/RESUME_BULLETS.md](docs/RESUME_BULLETS.md) | Project bullets |
| [docs/ABOUT_TOPICS.md](docs/ABOUT_TOPICS.md) | Suggested GitHub topics |

**Suggested topics:** `python` · `nlp` · `chatbot` · `conversational-ai` · `machine-learning` · `tourism`

---

## Author

**Amaragani Nikhil Sai** · B.Tech CSE  
Portfolio: https://nikhilamaragani-jpg.github.io/  
LinkedIn: https://www.linkedin.com/in/nikhil-sai-amaragani-219115382  
Email: nikhilamaragani@gmail.com

## License

MIT — see [LICENSE](LICENSE).
