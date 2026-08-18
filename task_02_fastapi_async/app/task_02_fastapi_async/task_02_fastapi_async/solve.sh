#!/bin/bash
pip install aiosqlite
sed -i 's/import sqlite3/import aiosqlite as sqlite3/' app/api.py
sed -i 's/conn = sqlite3.connect/conn = await sqlite3.connect/' app/api.py
sed -i 's/cur.execute/await cur.execute/' app/api.py
sed -i 's/rows = cur.fetchall/rows = await cur.fetchall/' app/api.py
sed -i 's/conn.close()/await conn.close()/' app/api.py
