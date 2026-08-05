# AI-Driven Chatbot Framework for Smart Tourism

**B.Tech Major Project** | Conversational AI | NLP | Smart Tourism

A practical chatbot prototype for smart tourism assistance. It detects user intent, generates domain-specific responses, and stores conversation history in SQLite.

---

## Overview

This project implements a modular tourism chatbot that can handle queries related to hotels, attractions, food, transport, budget, and itinerary planning.

**Project Type:** Academic Prototype with working core modules  
**Status:** Runnable CLI chatbot + SQLite history

---

## Architecture

```text
User Input
    |
    v
+------------------+
| Intent Detection |  (keyword-based intent classification)
+------------------+
    |
    v
+------------------+
| Response Engine  |  (tourism-domain response templates)
+------------------+
    |
    v
+------------------+
| SQLite Database  |  (stores chat history)
+------------------+
    |
    v
Bot Reply + Optional History View
```

---

## Features

- Intent detection for multiple tourism categories
- Structured response generation
- SQLite-based conversation history
- Simple CLI interface
- Modular project structure for future NLP/RAG upgrades

---

## Tech Stack

| Area | Technology |
|------|------------|
| Language | Python |
| Intent Logic | Rule/keyword-based NLP |
| Storage | SQLite |
| Interface | Command Line |
| Tools | Git |

---

## Project Structure

```text
ai-driven-chatbot-smart-tourism/
├── README.md
├── requirements.txt
├── data/                  # SQLite DB created at runtime
├── src/
│   ├── main.py
│   ├── chatbot/
│   │   ├── intent.py
│   │   ├── response.py
│   │   ├── database.py
│   │   └── __init__.py
│   └── utils/
└── LICENSE
```

---

## How to Run

```bash
git clone https://github.com/nikhilamaragani-jpg/ai-driven-chatbot-smart-tourism.git
cd ai-driven-chatbot-smart-tourism

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

python src/main.py
```

**Commands inside chatbot:**
- Type normal travel questions
- Type `history` to view recent chats
- Type `exit` to quit

---

## Example

```text
You: hello
Bot (greeting): Hello! I am your Smart Tourism assistant...

You: best hotels in paris
Bot (hotel_query): I can help with hotel suggestions...

You: history
--- Recent Conversations ---
```

---

## Current Status

- [x] Problem definition
- [x] Modular architecture
- [x] Intent detection module
- [x] Response generation module
- [x] SQLite chat history
- [x] Runnable CLI prototype
- [ ] Advanced ML-based intent classification
- [ ] FastAPI interface
- [ ] RAG-based knowledge responses

---

## Learning Outcomes

- Conversational system design
- Intent classification basics
- Modular Python project structure
- SQLite integration for application data

---

## Author

**Amaragani Nikhil Sai**  
B.Tech in Computer Science and Engineering

- GitHub: [nikhilamaragani-jpg](https://github.com/nikhilamaragani-jpg)
- LinkedIn: [Amaragani Nikhil Sai](https://linkedin.com/in/amaraganinikhilsai)
- Email: nikhilamaragani@gmail.com

---

## License

MIT License
