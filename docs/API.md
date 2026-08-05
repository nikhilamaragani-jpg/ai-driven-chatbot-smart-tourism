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
  "retrieval_scores": [{ "key": "places to visit", "score": 0.42 }]
}
```

## `GET /history?limit=5`

Returns recent conversation rows.

## OpenAPI

Interactive: `/docs`  
Schema: `/openapi.json`
