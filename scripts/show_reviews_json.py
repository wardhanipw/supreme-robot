#!/usr/bin/env python3
import sqlite3
import json
from pathlib import Path

DB = Path('restaurant_reviews.db')
if not DB.exists():
    print(json.dumps({"error": f"Database {DB} not found. Run scripts/init_sqlite.sh first."}))
    raise SystemExit(1)

conn = sqlite3.connect(str(DB))
conn.row_factory = sqlite3.Row
cur = conn.cursor()

restaurants = [dict(r) for r in cur.execute('SELECT id, name, street_address, description FROM restaurant')]

reviews = [dict(rv) for rv in cur.execute('''
    SELECT id, restaurant_id, user_name, rating, review_text, review_date
    FROM review
    ORDER BY review_date
''')]

output = {"restaurants": restaurants, "reviews": reviews}
print(json.dumps(output, ensure_ascii=False, indent=2))

conn.close()
