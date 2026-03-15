# AGENTS.md

This is a Towlion application repository, scaffolded from the app-template.

## Structure

- `app/` — FastAPI backend with `main.py` entry point
- `app/alembic/` — Database migrations (Alembic)
- `deploy/` — Docker Compose configs and Caddyfile
- `frontend/` — Optional Next.js frontend (placeholder)
- `scripts/` — Deployment utilities (health check)
- `.github/workflows/` — CI/CD pipelines

## Key conventions

- Backend listens on port 8000
- `GET /health` must return `{"status": "ok"}`
- Configuration via environment variables (see `deploy/env.template`)
- Database: PostgreSQL with Alembic migrations
- Background jobs: Celery with Redis
- Object storage: MinIO (S3-compatible)

## Spec compliance

This repo should pass `python validator/validate.py --tier 2` from the [towlion/platform](https://github.com/towlion/platform) repo.
