<div align="center">

# AI-Driven Chatbot Framework for Smart Tourism

### B.Tech Major Project · Conversational AI · NLP · System Architecture

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Runnable%20Prototype-success)](https://github.com/nikhilamaragani-jpg/ai-driven-chatbot-smart-tourism)
[![Portfolio](https://img.shields.io/badge/Portfolio-Website-5b8cff)](https://nikhilamaragani-jpg.github.io/portfolio/)

**Author:** Amaragani Nikhil Sai (22X31A0513)  
**Institution:** Sri Indu Institute of Engineering and Technology (JNTUH)  
**Guide:** Ms. K. Mounika · Department of CSE · 2025–2026

[Run](#quick-start) · [Interview guide](docs/INTERVIEW.md) · [Demo](docs/DEMO.md) · [Report summary](docs/REPORT_SUMMARY.md) · [Resume bullets](docs/RESUME_BULLETS.md)

</div>

---

## Executive Summary (for recruiters)

Tourism is information-intensive. Travelers need 24/7 help with destinations, hotels, transport, packages, and follow-up questions. Many existing bots are **rule-only**, lose context, and fail at personalization.

This major project delivers:

1. A **systematic framing** of AI chatbots for smart tourism (classification, architecture, tools landscape, 6A tourism framework impact).
2. A **runnable modular chatbot** that demonstrates intent detection, knowledge-base answers, response generation, and **conversation logging**.

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

---

## Quick Start

```bash
git clone https://github.com/nikhilamaragani-jpg/ai-driven-chatbot-smart-tourism.git
cd ai-driven-chatbot-smart-tourism
pip install -r requirements.txt
python src/main.py
```

**Try:** `hello` · `places to visit` · `visa requirements` · `budget planning` · `history` · `help` · `exit`

---

## Documentation suite (elite portfolio pack)

| Doc | Purpose |
|-----|---------|
| [INTERVIEW.md](docs/INTERVIEW.md) | 60s pitch, Q&A, demo script |
| [DEMO.md](docs/DEMO.md) | Expected terminal walkthrough + mermaid |
| [REPORT_SUMMARY.md](docs/REPORT_SUMMARY.md) | Academic report condensed for recruiters |
| [RESUME_BULLETS.md](docs/RESUME_BULLETS.md) | Copy-ready resume / LinkedIn bullets |
| [CONTRIBUTING.md](docs/CONTRIBUTING.md) | Dev notes |
| [PROJECT_BRIEF.md](docs/PROJECT_BRIEF.md) | Hiring-manager brief |

---

## Skills Recruiters Care About

| Skill | Evidence in this repo |
|-------|------------------------|
| Problem decomposition | Tourism pain points → layered architecture |
| Conversational AI basics | Intent + knowledge + response pipeline |
| Software structure | Package modules, single entrypoint |
| Data persistence | SQLite history |
| Documentation | Full recruiter/interview pack |
| Product thinking | 6A framework / smart tourism framing |

---

## Author

**Amaragani Nikhil Sai**  
Portfolio: https://nikhilamaragani-jpg.github.io/portfolio/  
LinkedIn: https://www.linkedin.com/in/nikhil-sai-amaragani-219115382  
Email: nikhilamaragani@gmail.com

## License

MIT License — see [LICENSE](LICENSE).
