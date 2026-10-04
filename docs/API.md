# API reference

Base URL (local): `http://127.0.0.1:8000`

## `GET /health`

Returns service status.

## `POST /chat`

```json
{ "message": "places to visit" }
```

Response:

```json
{
  "reply": "...",
  "intent": "attraction_query",
  "source": "retrieval",
  "retrieval_scores": [{ "key": "places to visit", "score": 0.42 }],
  "conversation_id": 1
}
```

## `POST /feedback`

Submit or update a helpfulness vote for a chat response. Only one current vote
is stored per conversation, so resubmitting updates the vote rather than
inflating counts.

```json
{ "conversation_id": 1, "rating": "helpful" }
```

`rating` must be `helpful` or `not_helpful`. Returns `404` if the conversation
does not exist. Configure `API_KEY` to protect this route with `X-API-Key`.

## `GET /history?limit=5`

Returns recent conversation rows.

## `GET /analytics?days=30`

Returns aggregate usage metrics for the last 1–365 UTC calendar days, including
daily chat-turn volume, detected intent counts, response-source counts, and
submitted feedback counts/helpful rate. The helpful rate is `null` when no
feedback was submitted during the period.
Empty days are included with a count of `0`. Historical intent/source values are
split from the existing `intent|source` log field; older unclassified values
are reported as `unknown`.

Example response:

```json
{
  "days": 30,
  "total_chat_turns": 1,
  "daily_volume": [{ "date": "2026-10-03", "count": 1 }],
  "intent_counts": [{ "name": "attraction_query", "count": 1 }],
  "source_counts": [{ "name": "retrieval", "count": 1 }],
  "feedback_total": 1,
  "helpful_rate_pct": 100.0,
  "feedback_counts": [{ "name": "helpful", "count": 1 }]
}
```

## `GET /analytics/export.csv?days=30`

Downloads the same aggregate metrics as CSV (`date,metric,dimension,value`).
Neither analytics endpoint returns raw user messages or bot responses.

When `API_KEY` is configured, both analytics endpoints require the `X-API-Key`
header, like `/chat` and `/history`.

## OpenAPI

Interactive: `/docs`  
Schema: `/openapi.json`
