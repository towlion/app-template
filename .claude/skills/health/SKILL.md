---
disable-model-invocation: true
allowed-tools: Bash
description: Check the app health endpoint
---

# /health — Check Application Health

Check whether the application is running and healthy.

## Instructions

1. Try running `bash scripts/health-check.sh`
2. If that fails or doesn't exist, fall back to: `curl -sf http://localhost:8000/health`
3. Report the result to the user
4. If unhealthy, suggest checking container logs with `docker compose -f deploy/docker-compose.standalone.yml logs --tail 20`
