# Major project report summary

**Full title (academic report):**  
AI-Driven Chatbot Framework for Smart Tourism: A System Architecture and Systematic Review

| Field | Detail |
|-------|--------|
| Student | A. Nikhil Sai |
| Roll No. | **22X31A0513** |
| Degree | B.Tech — Computer Science and Engineering |
| Institution | Sri Indu Institute of Engineering and Technology (Autonomous), affiliated to **JNTUH** |
| Guide | **Ms. K. Mounika**, Assistant Professor |
| Department | CSE |
| Academic year | **2025–2026** |
| Report type | Major project report |

## Report goals (from abstract / objectives)

1. Classify chatbots and study conceptual architecture and components.  
2. Compare chatbot development tools (advantages / disadvantages).  
3. Examine chatbot integration in tourism over recent research.  
4. Analyze impact using the tourism **6A framework**:  
   **Attractions · Accessibility · Amenities · Activities · Available Packages · Ancillary Services**.  
5. Propose an AI-driven chatbot framework for smart tourism environments.

## Problem (report)

- Rule-based tourism bots with fixed scripts  
- Weak multi-turn context and personalization  
- Limited integration with booking / travel services  
- Limited multilingual and cultural adaptability  

## Proposed architecture layers (report design)

| Layer | Role |
|-------|------|
| User interface | Web / mobile natural-language interaction |
| Chatbot processing | NLP, intent, entity extraction |
| AI / ML | Recommendations and smarter responses |
| Database | Destinations, hotels, packages, interactions |
| Integration | External tourism / booking services |
| Response generation | Final answer to the user |

## Report modules (design)

User interface · Query processing · Recommendation · Database management · Integration · Response generation

## Report tech vision

AI / ML / Deep Learning / NLP · DBMS (e.g. MySQL in report) · Web stack (HTML/CSS/JS) · API integration · (report sample code includes Django models and optional OpenAI-style generation)

## UI screens listed in report

Welcome · Create account · Login · Chatbot · Dashboard · Profile

## UML (report)

System architecture · Use case · Class · Sequence · Activity diagrams

---

## Honest mapping: report vs this GitHub repository

| Area | Academic report | This repository (runnable demo) |
|------|-----------------|----------------------------------|
| Scope | Full major-project research + system design + sample web-oriented code | Focused **modular prototype** you can clone and run |
| Interface | Web screens (login, dashboard, profile) | **CLI** + **FastAPI** REST (`/chat`, `/history`, `/health`) |
| NLP / AI | Broad NLP / ML / optional LLM generation | **RAG-style TF-IDF / hashing retrieval** + intent templates; optional LLM hooks documented |
| Data | Tourism DB models (destinations, hotels, packages, bookings) | Curated **knowledge base** + **SQLite** conversation log |
| Multilingual | Report objective | Partial roadmap / sample report code; not full production i18n here |
| Booking APIs | Report integration vision | **Not implemented** (roadmap) |

**Use this file** when explaining the project: the report is the academic depth; the repo is the engineering evidence that runs offline.
