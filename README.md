<div align="center">

# AI-Driven Chatbot Framework for Smart Tourism

### B.Tech Major Project · Conversational AI · NLP · System Architecture

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Runnable%20Prototype-success)](https://github.com/nikhilamaragani-jpg/ai-driven-chatbot-smart-tourism)
[![Domain](https://img.shields.io/badge/Domain-Smart%20Tourism-blue)](https://github.com/nikhilamaragani-jpg/ai-driven-chatbot-smart-tourism)

**Author:** Amaragani Nikhil Sai (22X31A0513)  
**Institution:** Sri Indu Institute of Engineering and Technology (JNTUH)  
**Guide:** Ms. K. Mounika · Department of CSE · 2025–2026

[Run](#quick-start) · [Architecture](#system-architecture) · [Skills demonstrated](#skills-recruiters-care-about) · [Docs](docs/PROJECT_BRIEF.md)

</div>

---

## Executive Summary (for recruiters)

Tourism is information-intensive. Travelers need 24/7 help with destinations, hotels, transport, packages, and follow-up questions. Many existing bots are **rule-only**, lose context, and fail at personalization.

This major project delivers:

1. A **systematic framing** of AI chatbots for smart tourism (classification, architecture, tools landscape, 6A tourism framework impact).
2. A **runnable modular chatbot** that demonstrates intent detection, knowledge-base answers, response generation, and **conversation logging**.

The implementation is intentionally clean and extensible toward NLP engines, multilingual support, and booking APIs described in the full report.

---

## Problem Statement

| Gap in existing systems | What this project targets |
|-------------------------|---------------------------|
| Keyword / script-only bots | Intent-based routing |
| No conversation memory | Session-style multi-turn CLI + history |
| Generic answers | Knowledge-base tourism FAQs & recommendations |
| Weak analytics | SQLite chat history for review |
| Isolated tools | Modular layers ready for API integration |

---

## Objectives (from project report)

- Design an AI-oriented tourism chatbot that supports natural-language queries
- Provide destination / hotel / activity style assistance via structured knowledge
- Support multi-turn interaction without forcing users to restart context every time
- Persist interactions for analysis and continuous improvement
- Keep architecture aligned with smart tourism needs (personalization, 24/7 support, integration readiness)

---

## System Architecture

```text
User (CLI today · Web UI tomorrow)
              |
              v
┌─────────────────────────────┐
│  Query Processing Layer     │  Intent detection (keyword / rule NLP-style)
└─────────────────────────────┘
              |
              v
┌─────────────────────────────┐
│  Knowledge + Logic Layer    │  FAQ match · recommendations · tourism content
└─────────────────────────────┘
              |
              v
┌─────────────────────────────┐
│  Response Generation        │  Templates · structured natural replies
└─────────────────────────────┘
              |
              v
┌─────────────────────────────┐
│  Persistence (SQLite)       │  Conversation history · metadata
└─────────────────────────────┘
```

**Report-aligned components:** preprocessing concepts · NLP/intent · knowledge base · context management · response generation · analytics hooks · external integration points (hotels/airlines/packages).

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3 |
| Core design | Modular package (`src/chatbot/`) |
| Storage | SQLite |
| Interface | CLI (demo) |
| Report stack vision | AI/ML/NLP · DBMS · HTML/CSS/JS · APIs |

---

## Repository Structure

```text
ai-driven-chatbot-smart-tourism/
├── docs/
│   └── PROJECT_BRIEF.md      # Report-aligned brief for hiring managers
├── src/
│   ├── main.py               # CLI entry
│   └── chatbot/
│       ├── intent.py         # Intent classification
│       ├── knowledge.py      # Tourism knowledge base
│       ├── response.py       # Response generation
│       └── database.py       # Chat history (SQLite)
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Quick Start

```bash
git clone https://github.com/nikhilamaragani-jpg/ai-driven-chatbot-smart-tourism.git
cd ai-driven-chatbot-smart-tourism
pip install -r requirements.txt
python src/main.py
```

**Try:**
- `hello` / `hi`
- `best hotels in paris` / `places to visit`
- `visa requirements` / `how to reach`
- `history`
- `exit`

---

## Features

- [x] Intent-based query routing for tourism domains
- [x] Knowledge-base driven answers (destinations, hotels, activities concepts)
- [x] Structured response generation
- [x] Persistent conversation logging
- [x] Modular code layout for extension
- [ ] Transformer / LLM backend
- [ ] Multilingual support
- [ ] Live booking / travel API integrations
- [ ] Web dashboard (report screens: welcome, auth, chatbot, profile)

---

## Skills Recruiters Care About

| Skill | Evidence in this repo |
|-------|------------------------|
| Problem decomposition | Tourism pain points → layered architecture |
| Conversational AI basics | Intent + knowledge + response pipeline |
| Software structure | Package modules, single entrypoint |
| Data persistence | SQLite history |
| Documentation | Report-aligned README + brief |
| Product thinking | 6A framework / smart tourism framing |

---

## Academic Context

- **Type:** B.Tech Major Project Report + implementation prototype
- **College:** Sri Indu Institute of Engineering and Technology
- **Affiliation:** JNTUH
- **Student:** A. Nikhil Sai · Roll No. 22X31A0513

Full report PDF available on request / portfolio materials.

---

## Author

**Amaragani Nikhil Sai**  
B.Tech CSE · Aspiring AI / Data / Intelligent Systems Engineer  

- GitHub: [nikhilamaragani-jpg](https://github.com/nikhilamaragani-jpg)
- LinkedIn: [nikhil-sai-amaragani](https://www.linkedin.com/in/nikhil-sai-amaragani-219115382)
- Email: nikhilamaragani@gmail.com

---

## License

MIT License — see [LICENSE](LICENSE).
