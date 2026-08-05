# AI-Driven Chatbot Framework for Smart Tourism

**B.Tech Major Project** | Conversational AI | NLP | Smart Tourism System Architecture

A practical chatbot prototype for smart tourism assistance featuring intent detection, knowledge-base FAQs, structured responses, and SQLite conversation history. This implementation draws from a systematic review of AI chatbots in tourism and a proposed multi-layer framework.

---

## Overview

The system helps travelers with destination information, hotels, activities, and common queries. Core capabilities:

- Intent classification for tourism queries
- Knowledge base matching for FAQs and recommendations
- Context-aware response generation
- Persistent chat history via SQLite
- Extensible design toward NLP engines and external integrations

**Status:** Runnable CLI chatbot with knowledge base + database logging  
**Project Focus:** System architecture, knowledge management, and conversational flow for smart tourism

---

## System Architecture (Aligned with Project Report)

```text
User Interface (CLI / future Web)
        |
        v
+---------------------------+
| Query Processing Layer    |  Intent detection + NLP-style parsing
+---------------------------+
        |
        v
+---------------------------+
| Knowledge Base + AI Layer |  FAQ match + recommendation logic
+---------------------------+
        |
        v
+---------------------------+
| Response Generation       |  Structured, readable replies
+---------------------------+
        |
        v
+---------------------------+
| Database Layer (SQLite)   |  Conversation history & metadata
+---------------------------+
```

Key components inspired by the full framework: data preprocessing concepts, knowledge bases, context management, response generation, and future integration points (booking systems, multi-language support).

---

## Tech Stack

| Area              | Technology                          |
|-------------------|-------------------------------------|
| Language          | Python 3                            |
| Core Logic        | Custom intent + knowledge modules   |
| Storage           | SQLite                              |
| Future Extensions | NLP libraries, OpenAI-style APIs, Django/web UI |

---

## Project Structure

```text
ai-driven-chatbot-smart-tourism/
├── src/
│   ├── main.py                 # CLI entry point
│   └── chatbot/
│       ├── intent.py           # Keyword / rule-based intent detection
│       ├── knowledge.py        # Tourism FAQ & recommendation knowledge base
│       ├── response.py         # Response templates & generation
│       └── database.py         # SQLite chat history
├── requirements.txt
└── README.md
```

---

## How to Run

```bash
git clone https://github.com/nikhilamaragani-jpg/ai-driven-chatbot-smart-tourism.git
cd ai-driven-chatbot-smart-tourism
pip install -r requirements.txt
python src/main.py
```

**Sample interactions:**
- `hello` / `hi`
- `best hotels in paris` / `places to visit`
- `visa requirements` / `how to reach`
- `history` (view conversation log)
- `exit`

---

## Key Features from Project Scope

- Intent-based routing for tourism queries
- Knowledge-base driven answers (destinations, hotels, activities concepts)
- Persistent logging for analytics / review
- Modular design ready for NLP upgrades and external API integration
- Focus on real-time information delivery and personalization potential

---

## Future Enhancements (from Project Report)

- Integration of advanced LLMs / transformer models
- Multi-language support and translation
- Voice interface
- Sentiment-aware responses
- Booking / travel platform integrations
- Predictive recommendations and analytics

---

## Author

**Amaragani Nikhil Sai**  
B.Tech in Computer Science and Engineering  
Sri Indu Institute of Engineering and Technology

- GitHub: [nikhilamaragani-jpg](https://github.com/nikhilamaragani-jpg)
- LinkedIn: [Amaragani Nikhil Sai](https://linkedin.com/in/amaraganinikhilsai)
- Email: nikhilamaragani@gmail.com

---

## License

MIT License
