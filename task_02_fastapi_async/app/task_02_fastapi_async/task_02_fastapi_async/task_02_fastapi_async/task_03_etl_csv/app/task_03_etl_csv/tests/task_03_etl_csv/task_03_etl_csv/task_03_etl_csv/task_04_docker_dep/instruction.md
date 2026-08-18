# Task: Fix Docker Compose Healthcheck and Redis Connection

## Problem
The FastAPI service crashes on startup in Docker Compose. 

Error: `redis.exceptions.ConnectionError: Error 111 connecting to localhost:6379. Connection refused.`

The `/health` endpoint also returns 500 when Redis is temporarily down instead of returning a graceful 503.

## Requirements
1. The app must connect to Redis correctly inside Docker Compose
2. `/health` must return `{"status": "ok"}` with 200 if Redis is up
3. `/health` must return `{"status": "unhealthy"}` with 503 if Redis is down
4. All existing tests in `tests/test_main.py` must pass
5. Do not change the API routes

## Notes
- Use only libraries already in `requirements.txt`
- The solution must work with `docker compose up`
- Redis service name in docker-compose is `redis`
