#!/bin/bash
# This script fixes the redis host and adds proper healthcheck error handling

cat > app/main.py << 'EOF'
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import redis

app = FastAPI()

# FIX: Use 'redis' as hostname because that's the service name in docker-compose
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.get("/health")
def health():
    # FIX: Gracefully handle redis being down
    try:
        r.ping()
        return {"status": "ok"}
    except redis.ConnectionError:
        return JSONResponse(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, content={"status": "unhealthy"})

@app.get("/count")
def count():
    val = r.get("counter")
    return {"count": int(val) if val else 0}
EOF

echo "Fix applied: Changed redis host to 'redis' and added 503 healthcheck"
