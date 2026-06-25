#!/usr/bin/env python3
"""
Display reviews from database in a nicely formatted table with borders.
Uses the 'rich' library for beautiful terminal output.
"""
import sqlite3
from pathlib import Path
from rich.console import Console
from rich.table import Table

DB = Path('restaurant_reviews.db')
if not DB.exists():
    print(f"Database {DB} not found. Run scripts/init_sqlite.sh first.")
    raise SystemExit(1)

console = Console()

# Connect to database
conn = sqlite3.connect(str(DB))
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Display Restaurants
console.print("\n[bold cyan]RESTAURANTS[/bold cyan]")
restaurant_table = Table(title="Restaurant List", show_header=True, header_style="bold magenta")
restaurant_table.add_column("ID", style="cyan", width=5)
restaurant_table.add_column("Name", style="green")
restaurant_table.add_column("Address", style="yellow")
restaurant_table.add_column("Description", style="white")

for r in cur.execute('SELECT id, name, street_address, description FROM restaurant'):
    restaurant_table.add_row(
        str(r['id']),
        r['name'] or "",
        r['street_address'] or "",
        r['description'] or ""
    )

console.print(restaurant_table)

# Display Reviews
console.print("\n[bold cyan]REVIEWS[/bold cyan]")
review_table = Table(title="Reviews", show_header=True, header_style="bold magenta")
review_table.add_column("ID", style="cyan", width=5)
review_table.add_column("Restaurant", style="green")
review_table.add_column("User", style="yellow")
review_table.add_column("Rating", style="white", width=8)
review_table.add_column("Review Text", style="white")
review_table.add_column("Date", style="blue")

for rv in cur.execute('''
    SELECT review.id, restaurant.name as restaurant, review.user_name, review.rating, review.review_text, review.review_date
    FROM review JOIN restaurant ON review.restaurant_id = restaurant.id
    ORDER BY review.review_date;
'''):
    # Add star rating visualization
    rating_stars = "⭐" * rv['rating']
    
    review_table.add_row(
        str(rv['id']),
        rv['restaurant'] or "",
        rv['user_name'] or "",
        f"{rating_stars} ({rv['rating']}/5)",
        rv['review_text'] or "",
        rv['review_date'] or ""
    )

console.print(review_table)

conn.close()
