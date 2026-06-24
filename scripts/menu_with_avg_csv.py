#!/usr/bin/env python3
import sqlite3
import csv
from pathlib import Path

DB = Path('restaurant_reviews.db')
OUTDIR = Path('output')
OUTDIR.mkdir(exist_ok=True)
OUT = OUTDIR / 'restaurants_with_menu.csv'

if not DB.exists():
    print(f"Database {DB} not found. Run scripts/init_sqlite.sh first.")
    raise SystemExit(1)

conn = sqlite3.connect(str(DB))
conn.row_factory = sqlite3.Row
cur = conn.cursor()

with OUT.open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # header
    writer.writerow([
        'restaurant_id', 'restaurant_name', 'street_address', 'restaurant_description',
        'avg_rating', 'menu_id', 'menu_name', 'menu_price', 'menu_description'
    ])

    cur.execute('SELECT id, name, street_address, description FROM restaurant ORDER BY id')
    for r in cur.fetchall():
        rid = r['id']
        cur.execute('SELECT AVG(rating) as avg_rating FROM review WHERE restaurant_id = ?', (rid,))
        avg = cur.fetchone()[0]
        avg_val = round(avg,2) if avg is not None else ''
        cur.execute('SELECT id, name, price, description FROM menu WHERE restaurant_id = ? ORDER BY id', (rid,))
        menus = cur.fetchall()
        if menus:
            for m in menus:
                writer.writerow([
                    rid, r['name'], r['street_address'], r['description'],
                    avg_val, m['id'], m['name'], m['price'], m['description']
                ])
        else:
            writer.writerow([rid, r['name'], r['street_address'], r['description'], avg_val, '', '', '', ''])

print(f"CSV written to {OUT}")
conn.close()
