# AI-Driven Chatbot Framework for Smart Tourism

**B.Tech Major Project** | Conversational AI | NLP | Smart Tourism

A practical chatbot prototype for smart tourism assistance with intent detection, FAQ knowledge base, and SQLite conversation history.

---

## Overview

The chatbot can:
- Detect tourism-related intents
- Answer common FAQs from a knowledge base
- Generate structured responses
- Store chat history in SQLite

**Status:** Runnable CLI chatbot with knowledge base + database

---

## Architecture

```text
User Input
    |
    +--> Knowledge Base match? --> FAQ answer
    |
    +--> Intent Detection --> Response Engine
    |
    v
SQLite Chat History
```

---

## Project Structure

```text
ai-driven-chatbot-smart-tourism/
├── src/
│   ├── main.py
│   └── chatbot/
│       ├── intent.py
│       ├── response.py
│       ├── knowledge.py
│       └── database.py
├── data/
├── requirements.txt
└── README.md
```

---

## How to Run

```bash
pip install -r requirements.txt
python src/main.py
```

Try questions like:
- `hello`
- `best hotels in paris`
- `visa requirements`
- `history`
- `exit`

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
