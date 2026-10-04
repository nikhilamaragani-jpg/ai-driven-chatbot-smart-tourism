# Evaluation (Applied AI)

## Offline retrieval eval

```bash
python scripts/evaluate_retrieval.py
```

Outputs `data/outputs/retrieval_eval.json` with hit-rate over labeled queries.

## Usage analytics

For product-analysis demos, `POST /feedback` records a `helpful` or
`not_helpful` vote against a chat response. `GET /analytics?days=30` summarizes
chat-turn volume by UTC date, detected intent, response source, feedback counts,
and helpfulness rate. The requested window can range from 1 to 365 calendar
days; days without activity are returned as zero. `GET /analytics/export.csv?days=30`
exports these aggregates for spreadsheet or notebook analysis without exporting
message content. The feedback and analytics endpoints require `X-API-Key` when
`API_KEY` is configured.

These metrics describe usage of the local prototype's SQLite log; they do not
represent live tourism demand or external booking activity.

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
