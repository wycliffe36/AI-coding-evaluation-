import csv
import sqlite3
import sys

def import_users(csv_path, db_path="db.sqlite"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")

    with open(csv_path, "r") as f: # BUG 1: no encoding for UTF-8 names
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("INSERT INTO users VALUES (?,?,?)", (row['id'], row['name'], row['email']))
    conn.close() # BUG 2: forgot to commit, so nothing saves

if __name__ == "__main__":
    import_users(sys.argv[1])
