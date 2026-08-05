# Contributing / Development Notes

This is primarily an academic + portfolio repository. Contributions that improve clarity, tests, or demo quality are welcome.

## Local setup

```bash
git clone https://github.com/nikhilamaragani-jpg/ai-driven-chatbot-smart-tourism.git
cd ai-driven-chatbot-smart-tourism
pip install -r requirements.txt
python src/main.py
```

## Code layout

- `src/chatbot/intent.py` — keyword intent detection
- `src/chatbot/knowledge.py` — tourism FAQ knowledge base
- `src/chatbot/response.py` — response templates
- `src/chatbot/database.py` — SQLite history
- `src/main.py` — CLI entry

## Good first improvements

- Unit tests for intent detection
- JSON knowledge base external file
- Simple FastAPI wrapper
- Better multi-turn context memory

## Scope honesty

Please keep README status checkboxes accurate. Do not claim production LLM accuracy without evaluation evidence.
