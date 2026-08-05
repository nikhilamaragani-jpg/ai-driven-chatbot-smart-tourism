# Prompt engineering notes

Grounded template used when an LLM provider is enabled (`src/chatbot/llm.py`):

```text
You are a careful tourism assistant. Answer using ONLY the context.
If context is insufficient, say what extra detail you need.

Context:
- ...

User question: ...
Answer:
```

Design goals:

- Reduce hallucination for FAQ tourism help  
- Keep retrieval as the source of truth  
- Separate orchestration (service) from generation (llm module)  
