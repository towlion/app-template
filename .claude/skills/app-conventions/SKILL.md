---
user-invocable: false
description: Use when writing code, adding features, or modifying the app
---

# Towlion App Conventions

Key conventions for Towlion application repositories:

## FastAPI Backend
- Entry point: `app/main.py` with a `FastAPI()` instance
- Run with: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
- Must expose `GET /health` returning `{"status": "ok"}` with HTTP 200

## Project Layout
- `app/` — Python backend (FastAPI)
  - `app/__init__.py` must exist (required for `from app.models import Base` in alembic)
- `deploy/` — Docker Compose, Caddyfile, env.template
- `scripts/` — Utility scripts (health-check.sh)
- `frontend/` — Optional Next.js frontend

## Dependencies
- `requirements.txt` at repo root (not inside `app/`)
- Must include `fastapi` and `uvicorn`
- Dockerfile build context is `..` (repo root) to access both `requirements.txt` and `app/`

## Database
- PostgreSQL via SQLAlchemy
- Migrations with Alembic (`app/alembic/`)
- Connection via `DATABASE_URL` env var

## Background Tasks
- Celery with Redis as broker
- Workers run as separate containers
- Connection via `REDIS_URL` env var

## Environment Variables
- All config via env vars, never hardcode secrets
- Template in `deploy/env.template`
- Required: `APP_DOMAIN`, `DATABASE_URL`, `REDIS_URL`

## Commit Convention
- Format: `type: description` (lowercase type, no scope)
- Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`
- No Conventional Commits scope syntax — just `type: description`

## Docker
- Two compose files: `docker-compose.yml` (multi-app), `docker-compose.standalone.yml` (full stack)
- App container exposes port 8000
- Include healthcheck in compose definition
- Dockerfile installs `curl` (required for healthcheck) and sets `ENV PYTHONPATH=/app` (required for alembic)
