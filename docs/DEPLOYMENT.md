# Deployment notes

## Local Docker

```bash
docker compose up --build
# http://localhost:8000/docs
```

## Cloud (TODO — not claimed live)

Recommended free-tier style targets:

1. **Render / Railway / Fly.io** — deploy Docker image, set env vars  
2. **Azure App Service / AWS App Runner** — when cloud practice is needed  

### Env for secure demo

```bash
API_KEY=replace-me
APP_ENV=production
LOG_LEVEL=INFO
```

Clients must send `X-API-Key`.

## Health check

`GET /health` — use for container probes.
