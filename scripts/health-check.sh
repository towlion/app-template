#!/usr/bin/env bash
set -euo pipefail

URL="${1:-http://localhost:8000/health}"
MAX_ATTEMPTS=30
INTERVAL=2

for i in $(seq 1 "$MAX_ATTEMPTS"); do
    if curl -sf "$URL" > /dev/null 2>&1; then
        echo "Health check passed (attempt $i/$MAX_ATTEMPTS)"
        exit 0
    fi
    echo "Waiting for service... ($i/$MAX_ATTEMPTS)"
    sleep "$INTERVAL"
done

echo "Health check failed after $MAX_ATTEMPTS attempts"
exit 1
