import pandas as pd
import sqlite3

def import_csv_to_db(csv_path, db_path):
    # BUG: Loads entire 100k+ row CSV into memory at once
    # This will OOM on large files
    df = pd.read_csv(csv_path)
    
    conn = sqlite3.connect(db_path)
    df.to_sql('users', conn, if_exists='replace', index=False)
    conn.close()
    
    return len(df)

if __name__ == "__main__":
    import_csv_to_db("data/large_users.csv", "db.sqlite")
