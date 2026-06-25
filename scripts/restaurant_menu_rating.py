#!/usr/bin/env python3
"""
Display each restaurant with its menu and average rating from reviews.
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

console.print("\n[bold cyan]RESTAURANTS WITH MENU AND AVERAGE RATING[/bold cyan]")
console.print("[yellow]Display each restaurant with its menu and the average rating from its reviews[/yellow]\n")

# Get all restaurants
restaurants = cur.execute('''
    SELECT DISTINCT r.id, r.name, r.street_address, r.description
    FROM restaurant r
    ORDER BY r.name
''').fetchall()

for restaurant in restaurants:
    rest_id = restaurant['id']
    rest_name = restaurant['name']
    rest_address = restaurant['street_address']
    
    # Get average rating for this restaurant
    avg_rating = cur.execute('''
        SELECT AVG(rating) as avg_rating, COUNT(*) as total_reviews
        FROM review
        WHERE restaurant_id = ?
    ''', (rest_id,)).fetchone()
    
    avg_rating_val = avg_rating['avg_rating'] or 0
    total_reviews = avg_rating['total_reviews'] or 0
    rating_stars = "⭐" * round(avg_rating_val) if avg_rating_val > 0 else "No ratings"
    
    # Create main table for restaurant info
    main_table = Table(
        title=f"{rest_name} | {rating_stars} ({avg_rating_val:.1f}/5) | {total_reviews} reviews",
        show_header=True,
        header_style="bold magenta",
        box=box.ROUNDED,
        style="cyan"
    )
    
    main_table.add_column("Item", style="green", width=20)
    main_table.add_column("Price", style="cyan", width=12)
    main_table.add_column("Description", style="white")
    
    # Get menu items for this restaurant
    menu_items = cur.execute('''
        SELECT id, name, price, description
        FROM menu
        WHERE restaurant_id = ?
        ORDER BY price
    ''', (rest_id,)).fetchall()
    
    if menu_items:
        for item in menu_items:
            main_table.add_row(
                item['name'][:20],
                f"Rp {item['price']:>10,.0f}",
                item['description'][:50] or ""
            )
    else:
        main_table.add_row("No menu items", "", "")
    
    console.print(main_table)
    console.print()

conn.close()
