# Demo walkthrough (5 minutes)

## Setup

```bash
pip install -r requirements.txt
python src/main.py
```

## Script

1. `hello` — greeting / intent path  
2. `visa requirements` — retrieval path  
3. `metro tips` — transport knowledge  
4. `budget planning` — practical FAQ  
5. `history` — show SQLite audit trail  
6. Optional API:

```bash
uvicorn src.api.app:app --reload
curl -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d "{\"message\":\"packing list\"}"
```

## Talking points

- Why TF-IDF first (zero API cost, deterministic demo)
- How you would swap in embeddings + vector DB
- What you log and why (evaluation, debugging)
