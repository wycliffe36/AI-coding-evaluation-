# Task: Fix ETL CSV Import Memory Crash

## Problem
The `import_csv_to_db` function in `app/etl.py` crashes with `MemoryError` when processing CSV files larger than ~50k rows.

Customer reports the job dies on production with a 100k+ row file. Server only has 2GB RAM.

## Requirements
1. The function must successfully import the entire CSV into the `users` table in SQLite
2. The process must not use more than 500MB of RAM regardless of CSV size
3. All existing tests in `tests/test_etl.py` must pass
4. Do not change the function signature: `import_csv_to_db(csv_path, db_path)`

## Notes
- Use only libraries already in `requirements.txt`
- The solution must be reproducible via Docker
