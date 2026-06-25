#!/usr/bin/env python3
"""
Display restaurant menus with average rating in formatted table.
"""
import sqlite3
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich import box

DB = Path('restaurant_reviews.db')
if not DB.exists():
    print(f"Database {DB} not found. Run scripts/init_sqlite.sh first.")
    raise SystemExit(1)

console = Console()
conn = sqlite3.connect(str(DB))
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Get all restaurants with menus
restaurants = cur.execute('''
    SELECT DISTINCT r.id, r.name, r.street_address, r.description
    FROM restaurant r
    ORDER BY r.name
''').fetchall()

for restaurant in restaurants:
    rest_id = restaurant['id']
    rest_name = restaurant['name']
    
    # Get average rating for this restaurant
    avg_rating = cur.execute('''
        SELECT AVG(rating) as avg_rating
        FROM review
        WHERE restaurant_id = ?
    ''', (rest_id,)).fetchone()['avg_rating'] or 0
    
    rating_stars = "⭐" * round(avg_rating) if avg_rating > 0 else "No ratings"
    
    # Create table with restaurant info
    table = Table(
        title=f"{rest_name} - {rating_stars} ({avg_rating:.1f}/5)" if avg_rating > 0 else f"{rest_name}",
        show_header=True,
        header_style="bold magenta",
        box=box.ROUNDED
    )
    
    table.add_column("Item", style="green", width=20)
    table.add_column("Price", style="cyan", width=10)
    table.add_column("Description", style="white")
    
    # Get menu items
    menu_items = cur.execute('''
        SELECT id, name, price, description
        FROM menu
        WHERE restaurant_id = ?
        ORDER BY price
    ''', (rest_id,)).fetchall()
    
    if menu_items:
        for item in menu_items:
            table.add_row(
                item['name'][:20],
                f"Rp {item['price']:,.0f}",
                item['description'][:40] or ""
            )
    else:
        table.add_row("No menu items", "", "")
    
    console.print(table)
    console.print()

conn.close()
