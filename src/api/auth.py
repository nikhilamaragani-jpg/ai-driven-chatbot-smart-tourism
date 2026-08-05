"""Optional API-key authentication for protected routes."""

from __future__ import annotations

from fastapi import Header, HTTPException, status

from config.settings import settings


def require_api_key(x_api_key: str | None = Header(default=None, alias="X-API-Key")) -> None:
    """
    If API_KEY is configured, require matching X-API-Key header.
    If API_KEY is empty, auth is disabled (local portfolio demo mode).
    """
    expected = (settings.api_key or "").strip()
    if not expected:
        return
    if not x_api_key or x_api_key.strip() != expected:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key. Pass header X-API-Key.",
        )
