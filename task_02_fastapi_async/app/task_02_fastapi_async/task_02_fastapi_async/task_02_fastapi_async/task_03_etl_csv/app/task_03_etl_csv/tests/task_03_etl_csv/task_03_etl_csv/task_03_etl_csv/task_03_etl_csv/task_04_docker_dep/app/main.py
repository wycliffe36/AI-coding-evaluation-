from fastapi import FastAPI
import redis

app = FastAPI()

# BUG: Missing healthcheck and wrong redis host
# Will fail in Docker because 'localhost' isn't the redis container
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.get("/health")
def health():
    # BUG: This will crash if redis is down instead of returning 503
    r.ping()
    return {"status": "ok"}

@app.get("/count")
def count():
    val = r.get("counter")
    return {"count": int(val) if val else 0}
