---
disable-model-invocation: true
allowed-tools: Bash
description: Deploy the app using Docker Compose
---

# /deploy — Deploy the Application

Build and start the application containers using Docker Compose.

## Instructions

1. Run: `docker compose -f deploy/docker-compose.standalone.yml up -d --build`
2. Wait a few seconds for containers to start
3. Run database migrations: `docker compose -f deploy/docker-compose.standalone.yml exec app alembic -c app/alembic.ini upgrade head`
4. Run the health check: `bash scripts/health-check.sh` or `curl -sf http://localhost:8000/health`
5. Report the result to the user
6. If the health check fails, check container logs: `docker compose -f deploy/docker-compose.standalone.yml logs --tail 20`
