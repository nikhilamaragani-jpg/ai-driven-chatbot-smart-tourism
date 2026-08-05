# Demo walkthrough

```bash
pip install -r requirements.txt
python src/main.py
```

Expected flow:

```text
============================================================
  Smart Tourism Chatbot  |  B.Tech Major Project Prototype
============================================================
You: hello
Bot (greeting): ...
You: places to visit
Bot (knowledge_faq / intent): ...
You: history
--- Recent Conversations ---
You: exit
```

```mermaid
flowchart TD
  A[User input] --> B{Knowledge FAQ?}
  B -->|Yes| C[FAQ answer]
  B -->|No| D[Detect intent]
  D --> E[Generate response]
  C --> F[Save SQLite]
  E --> F
  F --> G[Reply]
```
