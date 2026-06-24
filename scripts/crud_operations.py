#!/usr/bin/env python3
import sqlite3
import json
from pathlib import Path
from datetime import date

DB = Path('restaurant_reviews.db')
if not DB.exists():
    print(json.dumps({"error": f"Database {DB} not found. Run scripts/init_sqlite.sh first."}))
    raise SystemExit(1)

conn = sqlite3.connect(str(DB))
conn.row_factory = sqlite3.Row
cur = conn.cursor()

result = {}

# 1. CREATE
# Insert a new restaurant
cur.execute(
    "INSERT INTO restaurant (name, street_address, description) VALUES (?, ?, ?)",
    ("Soto Mantap", "Jl. Anggrek 9", "Soto ayam spesial")
)
new_restaurant_id = cur.lastrowid
result['insert_restaurant'] = {"id": new_restaurant_id}

# Insert a new review for an existing restaurant (use restaurant id 2 if exists)
cur.execute(
    "INSERT INTO review (restaurant_id, user_name, rating, review_text, review_date) VALUES (?, ?, ?, ?, ?)",
    (2, "Eka", 4, "Kopi enak dan pastry lezat", date.today().isoformat())
)
new_review_id = cur.lastrowid
result['insert_review'] = {"id": new_review_id}

conn.commit()

# 2. READ (Select)
def rows_to_list(r):
    return [dict(x) for x in r]

# Retrieve all reviews for a specific restaurant using restaurant_id = 1
cur.execute('SELECT * FROM review WHERE restaurant_id = ? ORDER BY review_date', (1,))
result['reviews_for_restaurant_1'] = rows_to_list(cur.fetchall())

# Retrieve all reviews with rating >= 4
cur.execute('SELECT * FROM review WHERE rating >= 4 ORDER BY review_date')
result['reviews_rating_4_plus'] = rows_to_list(cur.fetchall())

# Use a JOIN to display a list of restaurants along with their reviews
cur.execute('''
SELECT r.id as restaurant_id, r.name as restaurant_name, rv.id as review_id, rv.user_name, rv.rating, rv.review_text, rv.review_date
FROM restaurant r LEFT JOIN review rv ON rv.restaurant_id = r.id
ORDER BY r.id, rv.review_date
''')
result['restaurants_with_reviews'] = rows_to_list(cur.fetchall())

# 3. UPDATE
# Update the description of restaurant id 3
cur.execute('UPDATE restaurant SET description = ? WHERE id = ?', ("Nasi goreng dengan pilihan topping", 3))
result['update_restaurant_3'] = {"rows_affected": cur.rowcount}

# Update the rating of review id 2 to 5
cur.execute('UPDATE review SET rating = ? WHERE id = ?', (5, 2))
result['update_review_2'] = {"rows_affected": cur.rowcount}

conn.commit()

# 4. DELETE
# Delete one review based on id (delete review id 3 if exists)
cur.execute('DELETE FROM review WHERE id = ?', (3,))
result['delete_review_3'] = {"rows_affected": cur.rowcount}

# Delete a restaurant and ensure cascade (delete restaurant id 2)
cur.execute('DELETE FROM restaurant WHERE id = ?', (2,))
result['delete_restaurant_2'] = {"rows_affected": cur.rowcount}

conn.commit()

# 5. Additional Queries
# Highest-rated restaurant based on average rating
cur.execute('''
SELECT r.id, r.name, AVG(rv.rating) as avg_rating
FROM restaurant r JOIN review rv ON rv.restaurant_id = r.id
GROUP BY r.id, r.name
ORDER BY avg_rating DESC
LIMIT 1
''')
hr = cur.fetchone()
result['highest_rated_restaurant'] = dict(hr) if hr else None

# Number of reviews each restaurant has received
cur.execute('''
SELECT r.id, r.name, COUNT(rv.id) as review_count
FROM restaurant r LEFT JOIN review rv ON rv.restaurant_id = r.id
GROUP BY r.id, r.name
''')
result['review_counts'] = rows_to_list(cur.fetchall())

# Most recent review for each restaurant
cur.execute('''
SELECT r.id as restaurant_id, r.name as restaurant_name, rv.id as review_id, rv.user_name, rv.rating, rv.review_text, rv.review_date
FROM restaurant r
LEFT JOIN review rv ON rv.id = (
  SELECT id FROM review WHERE restaurant_id = r.id ORDER BY review_date DESC LIMIT 1
)
ORDER BY r.id
''')
result['most_recent_review_per_restaurant'] = rows_to_list(cur.fetchall())

print(json.dumps(result, ensure_ascii=False, indent=2))

conn.close()
