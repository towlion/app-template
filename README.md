# Towlion App Template

A template repository for bootstrapping new applications on the [Towlion platform](https://github.com/towlion/platform).

## Getting Started

1. Click **"Use this template"** on GitHub to create a new repository
2. Clone your new repo and configure environment variables
3. Build and deploy

## Project Structure

```
app/                    # FastAPI backend
  main.py               # Application entry point
  Dockerfile            # Backend container image
  models.py             # SQLAlchemy models
  tasks.py              # Celery background tasks
  alembic/              # Database migrations
deploy/
  docker-compose.yml    # App containers (multi-app mode)
  docker-compose.standalone.yml  # Full stack (self-hosted)
  Caddyfile             # Reverse proxy config
  env.template          # Environment variable reference
frontend/               # Optional Next.js frontend
scripts/
  health-check.sh       # Deployment health check
```

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn app.main:app --reload --port 8000

# Verify it works
curl http://localhost:8000/health
```

## Environment Variables

Copy `deploy/env.template` to `deploy/.env` and fill in your values. See the [platform spec](https://github.com/towlion/platform/blob/main/docs/spec.md) for details on required and optional variables.

## Deployment

### Multi-app mode (managed server)

Push to `main` to trigger the deploy workflow. The GitHub Action SSHs into the server and runs:

```bash
docker compose -f deploy/docker-compose.yml up -d --build
```

### Self-hosting (fork mode)

For standalone deployment on a single server:

```bash
cp deploy/env.template deploy/.env
# Edit deploy/.env with your values
docker compose -f deploy/docker-compose.standalone.yml up -d
```

This includes PostgreSQL, Redis, MinIO, and Caddy alongside your app.

## Deployment Secrets

Configure these GitHub Actions secrets on your repository (**Settings > Secrets and variables > Actions**):

| Secret | Required | Description |
|---|---|---|
| `SERVER_HOST` | Yes | Server IP address |
| `SERVER_USER` | Yes | SSH user (typically `deploy`) |
| `SERVER_SSH_KEY` | Yes | SSH private key for deployment |
| `APP_DOMAIN` | Yes | Application domain (e.g., `app.example.com`) |
| `PREVIEW_DOMAIN` | No | Base domain for PR preview environments (e.g., `example.com`) |

Database and storage credentials are auto-generated on the server by the bootstrap script. They are not GitHub secrets.

## Self-Hosting

For full self-hosting instructions, see the platform documentation:

- [Self-Hosting Guide](https://github.com/towlion/platform/blob/main/docs/self-hosting.md) — Fork model, server requirements, bootstrap process
- [Deployment Tutorial](https://github.com/towlion/platform/blob/main/docs/tutorial.md) — Step-by-step walkthrough from fork to running app

## License

[MIT](LICENSE)
