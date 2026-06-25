#!/usr/bin/env python3
"""
Display reviews filtered by restaurant name in a formatted table.
Usage: python3 scripts/show_reviews_by_restaurant.py [restaurant_name]
Example: python3 scripts/show_reviews_by_restaurant.py "Warung Makan"
"""
import sqlite3
import sys
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

# Get restaurant name from command line
if len(sys.argv) < 2:
    # Show all restaurants and ask user to choose
    console.print("\n[bold cyan]Available Restaurants:[/bold cyan]")
    restaurants = cur.execute('SELECT DISTINCT id, name FROM restaurant ORDER BY name').fetchall()
    
    rest_table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    rest_table.add_column("ID", style="cyan")
    rest_table.add_column("Name", style="green")
    
    for r in restaurants:
        rest_table.add_row(str(r['id']), r['name'])
    
    console.print(rest_table)
    console.print("\n[yellow]Usage: python3 scripts/show_reviews_by_restaurant.py <restaurant_name_or_id>[/yellow]")
    raise SystemExit(0)

search_term = sys.argv[1]

# Try to get restaurant by ID or name
restaurant = cur.execute('''
    SELECT id, name FROM restaurant 
    WHERE id = ? OR name LIKE ?
    LIMIT 1
''', (search_term if search_term.isdigit() else None, f'%{search_term}%')).fetchone()

if not restaurant:
    console.print(f"[red]Restaurant '{search_term}' not found[/red]")
    raise SystemExit(1)

rest_id = restaurant['id']
rest_name = restaurant['name']

# Get reviews for the restaurant
reviews = cur.execute('''
    SELECT review.id, review.user_name, review.rating, review.review_text, review.review_date
    FROM review
    WHERE review.restaurant_id = ?
    ORDER BY review.review_date DESC
''', (rest_id,)).fetchall()

# Display restaurant info
console.print(f"\n[bold cyan]Reviews for: {rest_name}[/bold cyan]")

if not reviews:
    console.print("[yellow]No reviews found for this restaurant[/yellow]")
    conn.close()
    raise SystemExit(0)

# Create and display table
review_table = Table(
    title=f"{rest_name} - All Reviews",
    show_header=True,
    header_style="bold magenta",
    box=box.ROUNDED
)

review_table.add_column("ID", style="cyan", width=5)
review_table.add_column("User", style="yellow", width=12)
review_table.add_column("Rating", style="white", width=12)
review_table.add_column("Review", style="white")
review_table.add_column("Date", style="blue", width=12)

for rv in reviews:
    rating_stars = "⭐" * rv['rating']
    review_table.add_row(
        str(rv['id']),
        rv['user_name'][:12] or "Anonymous",
        f"{rating_stars}\n({rv['rating']}/5)",
        rv['review_text'] or "No text",
        rv['review_date'] or ""
    )

console.print(review_table)

# Show stats for this restaurant
stats = cur.execute('''
    SELECT 
        COUNT(*) as total_reviews,
        AVG(rating) as avg_rating,
        MIN(rating) as min_rating,
        MAX(rating) as max_rating
    FROM review
    WHERE restaurant_id = ?
''', (rest_id,)).fetchone()

console.print("\n[bold cyan]Restaurant Statistics:[/bold cyan]")
stats_table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
stats_table.add_column("Metric", style="yellow")
stats_table.add_column("Value", style="green")

stats_table.add_row("Total Reviews", str(stats['total_reviews']))
stats_table.add_row("Average Rating", f"{'⭐' * round(stats['avg_rating'])}\n({stats['avg_rating']:.2f}/5)")
stats_table.add_row("Min Rating", f"{'⭐' * stats['min_rating']} ({stats['min_rating']}/5)")
stats_table.add_row("Max Rating", f"{'⭐' * stats['max_rating']} ({stats['max_rating']}/5)")

console.print(stats_table)

conn.close()
