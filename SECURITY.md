# Security Policy

## Reporting

If you discover a security issue in this academic/portfolio prototype, please email **nikhilamaragani@gmail.com** rather than opening a public issue.

## Scope notes

This repository is an educational demo. It is **not** production-hardened:
- No authentication hardening for multi-tenant SaaS
- SQLite is local-demo storage only
- Do not deploy with real traveler PII without a full security review

## Good practice when forking

- Never commit API keys or tokens
- Use environment variables for any future LLM/API integrations
- Sanitize logs before sharing demos
