# Evaluation (Applied AI)

## Offline retrieval eval

```bash
python scripts/evaluate_retrieval.py
```

Outputs `data/outputs/retrieval_eval.json` with hit-rate over labeled queries.

## Metrics to track in production (roadmap)

| Metric | Why |
|--------|-----|
| Retrieval hit-rate / precision@k | Is the right FAQ retrieved? |
| Groundedness checklist | Does answer stick to context? |
| Latency p50/p95 | API SLOs |
| Source mix | retrieval vs template vs llm |
| User thumbs-up (human) | Product quality |

## Sample artifact

See `data/outputs/retrieval_eval.sample.json`.
