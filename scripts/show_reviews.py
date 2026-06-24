#!/usr/bin/env python3
import sqlite3
from pathlib import Path

DB = Path('restaurant_reviews.db')
if not DB.exists():
    print(f"Database {DB} not found. Run scripts/init_sqlite.sh first.")
    raise SystemExit(1)

conn = sqlite3.connect(str(DB))
conn.row_factory = sqlite3.Row
cur = conn.cursor()

print('Restaurants:')
for r in cur.execute('SELECT id, name, street_address, description FROM restaurant'):
    print(f"{r['id']}: {r['name']} - {r['street_address']}")

print('\nReviews:')
for rv in cur.execute('''
    SELECT review.id, restaurant.name as restaurant, review.user_name, review.rating, review.review_text, review.review_date
    FROM review JOIN restaurant ON review.restaurant_id = restaurant.id
    ORDER BY review.review_date;
'''):
    print(f"{rv['id']}: {rv['restaurant']} - {rv['user_name']} ({rv['rating']}): {rv['review_text']} [{rv['review_date']}]")

conn.close()
