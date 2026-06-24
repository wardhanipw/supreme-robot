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

# Query: each restaurant with its menu and average rating from reviews
cur.execute('SELECT id, name, street_address, description FROM restaurant ORDER BY id')
restaurants = []
for r in cur.fetchall():
    rid = r['id']
    # menu items
    cur.execute('SELECT id, name, price, description FROM menu WHERE restaurant_id = ? ORDER BY id', (rid,))
    menu = [dict(m) for m in cur.fetchall()]
    # average rating
    cur.execute('SELECT AVG(rating) as avg_rating FROM review WHERE restaurant_id = ?', (rid,))
    avg = cur.fetchone()[0]
    restaurants.append({
        'id': rid,
        'name': r['name'],
        'street_address': r['street_address'],
        'description': r['description'],
        'avg_rating': round(avg,2) if avg is not None else None,
        'menu': menu
    })

print(json.dumps({'restaurants': restaurants}, ensure_ascii=False, indent=2))

conn.close()
