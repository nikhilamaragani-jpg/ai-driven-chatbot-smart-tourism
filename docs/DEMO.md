# Demo walkthrough

```bash
pip install -r requirements.txt
python src/main.py
```

```text
Smart Tourism Chatbot  |  B.Tech Major Project Prototype
You: hello
Bot: ...
You: places to visit
Bot: ...
You: history
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
```
