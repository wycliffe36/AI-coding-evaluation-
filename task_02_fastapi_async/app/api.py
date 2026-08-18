from fastapi import FastAPI
import sqlite3
import asyncio

app = FastAPI()

@app.get("/users")
async def get_users():
    conn = sqlite3.connect("db.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    conn.close()
    return {"users": rows}
