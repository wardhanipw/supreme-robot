#!/usr/bin/env python3
import sqlite3
import csv
from pathlib import Path

DB = Path('restaurant_reviews.db')
OUTDIR = Path('output')
OUTDIR.mkdir(exist_ok=True)
OUT_RESTAURANTS = OUTDIR / 'restaurants.csv'
OUT_MENU = OUTDIR / 'menu.csv'

if not DB.exists():
    print(f"Database {DB} not found. Run scripts/init_sqlite.sh first.")
    raise SystemExit(1)

conn = sqlite3.connect(str(DB))
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Export restaurants
with OUT_RESTAURANTS.open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'street_address', 'description'])
    cur.execute('SELECT id, name, street_address, description FROM restaurant ORDER BY id')
    for r in cur.fetchall():
        writer.writerow([r['id'], r['name'], r['street_address'], r['description']])

# Export menu
with OUT_MENU.open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'restaurant_id', 'name', 'price', 'description'])
    cur.execute('SELECT id, restaurant_id, name, price, description FROM menu ORDER BY id')
    for m in cur.fetchall():
        writer.writerow([m['id'], m['restaurant_id'], m['name'], m['price'], m['description']])

print(f"Written {OUT_RESTAURANTS} and {OUT_MENU}")
conn.close()
