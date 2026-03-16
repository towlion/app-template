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

## Background Tasks (opt-in, not default)
- Celery with Redis as broker
- Workers run as separate containers
- Connection via `REDIS_URL` env var
- Not included by default — see README for instructions to re-enable

## Environment Variables
- All config via env vars, never hardcode secrets
- Template in `deploy/env.template`
- Required: `APP_DOMAIN`, `DATABASE_URL`, `REDIS_URL`

## Commit Convention
- Format: `type: description` (lowercase type, no scope)
- Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`
- No Conventional Commits scope syntax — just `type: description`

## Structured Logging
- Uses `python-json-logger` — JSON logs to stdout
- Request middleware logs: method, path, status_code, duration_ms, client_ip
- Dockerfile uses `--no-access-log` (structured middleware replaces uvicorn access log)

## Rate Limiting
- Uses `slowapi`, default 60 requests/min per IP
- `/health` is exempt via `@limiter.exempt`
- All endpoints need `request: Request` parameter for slowapi

## Docker
- Two compose files: `docker-compose.yml` (multi-app), `docker-compose.standalone.yml` (full stack)
- App container exposes port 8000
- Include healthcheck in compose definition
- Dockerfile installs `curl` (required for healthcheck) and sets `ENV PYTHONPATH=/app` (required for alembic)
- Read-only filesystem: `read_only: true` + `tmpfs: [/tmp, /app/__pycache__]` in compose files
- BuildKit syntax, pip cache mount, build context is `..` (repo root)

## CI/CD — Reusable Workflows
- All 4 workflows (validate, ci, deploy, preview) call reusable workflows from `towlion/.github`
- Deploy/preview use `caddyfile-template` input with `__APP_DOMAIN__`/`__APP_NAME__` placeholders
- Preview also uses `__PR_NUMBER__`/`__PREVIEW_DOMAIN__` placeholders
