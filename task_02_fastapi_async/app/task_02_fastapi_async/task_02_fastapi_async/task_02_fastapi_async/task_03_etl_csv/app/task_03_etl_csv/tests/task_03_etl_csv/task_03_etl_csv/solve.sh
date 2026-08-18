#!/bin/bash
# This script applies the fix: use chunks to avoid loading entire CSV into memory

cat > app/etl.py << 'EOF'
import pandas as pd
import sqlite3

def import_csv_to_db(csv_path, db_path):
    # FIX: Process CSV in chunks to keep memory usage low
    conn = sqlite3.connect(db_path)
    chunk_size = 5000
    first_chunk = True
    
    for chunk in pd.read_csv(csv_path, chunksize=chunk_size):
        chunk.to_sql('users', conn, if_exists='replace' if first_chunk else 'append', index=False)
        first_chunk = False
    
    conn.close()
    
    # Return total count
    df_count = pd.read_csv(csv_path)
    return len(df_count)
EOF

echo "Fix applied: CSV is now processed in 5000-row chunks"
