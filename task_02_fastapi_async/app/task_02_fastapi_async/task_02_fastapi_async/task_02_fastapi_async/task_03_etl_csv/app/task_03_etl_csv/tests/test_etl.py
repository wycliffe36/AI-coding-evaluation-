import os
import sqlite3
import pandas as pd
import pytest
from app.etl import import_csv_to_db

@pytest.fixture
def big_csv(tmp_path):
    # Create a 100k row CSV to simulate OOM
    csv_path = tmp_path / "large_users.csv"
    df = pd.DataFrame({
        "id": range(100000),
        "email": [f"user{i}@test.com" for i in range(100000)],
        "data": ["x"*100 for i in range(100000)]
    })
    df.to_csv(csv_path, index=False)
    return str(csv_path)

def test_import_handles_large_csv(big_csv, tmp_path):
    db_path = tmp_path / "test.db"
    count = import_csv_to_db(big_csv, str(db_path))
    
    # Check it actually imported everything
    assert count == 100000
    
    # Check data is in DB
    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users")
    assert cur.fetchone()[0] == 100000
    conn.close()
