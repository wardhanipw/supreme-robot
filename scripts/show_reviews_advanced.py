#!/usr/bin/env python3
"""
Display reviews in different table format options.
Usage: python3 scripts/show_reviews_advanced.py [format]
Formats: rich (default), simple, grid, minimal
"""
import sqlite3
import sys
from pathlib import Path
from rich.console import Console
from rich.table import Table

DB = Path('restaurant_reviews.db')
if not DB.exists():
    print(f"Database {DB} not found. Run scripts/init_sqlite.sh first.")
    raise SystemExit(1)

# Get format from command line or use default
format_type = sys.argv[1] if len(sys.argv) > 1 else 'rich'

console = Console()
conn = sqlite3.connect(str(DB))
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Table style mappings
styles = {
    'rich': 'box.ROUNDED',
    'simple': 'box.SIMPLE',
    'double': 'box.DOUBLE',
    'minimal': 'box.MINIMAL',
    'heavy': 'box.HEAVY'
}

if format_type not in styles:
    console.print(f"[red]Unknown format '{format_type}'[/red]")
    console.print(f"Available formats: {', '.join(styles.keys())}")
    raise SystemExit(1)

# Import the appropriate box style
from rich import box
box_style = getattr(box, styles[format_type].split('.')[1])

# Display Reviews with selected format
console.print(f"\n[bold cyan]REVIEWS ({format_type.upper()})[/bold cyan]")
review_table = Table(
    title="Restaurant Reviews",
    show_header=True,
    header_style="bold magenta",
    box=box_style
)

review_table.add_column("ID", style="cyan", width=5)
review_table.add_column("Restaurant", style="green", width=15)
review_table.add_column("User", style="yellow", width=10)
review_table.add_column("Rating", style="white", width=10)
review_table.add_column("Review", style="white")
review_table.add_column("Date", style="blue", width=12)

for rv in cur.execute('''
    SELECT review.id, restaurant.name as restaurant, review.user_name, 
           review.rating, review.review_text, review.review_date
    FROM review JOIN restaurant ON review.restaurant_id = restaurant.id
    ORDER BY review.review_date DESC;
'''):
    rating_stars = "⭐" * rv['rating']
    review_table.add_row(
        str(rv['id']),
        rv['restaurant'][:15] or "",
        rv['user_name'][:10] or "",
        f"{rating_stars}\n({rv['rating']}/5)",
        rv['review_text'][:40] or "",
        rv['review_date'] or ""
    )

console.print(review_table)

# Show statistics
console.print("\n[bold cyan]STATISTICS[/bold cyan]")
stats = cur.execute('''
    SELECT 
        COUNT(*) as total_reviews,
        AVG(rating) as avg_rating,
        COUNT(DISTINCT restaurant_id) as restaurants
    FROM review;
''').fetchone()

stats_table = Table(show_header=True, header_style="bold magenta", box=box_style)
stats_table.add_column("Metric", style="yellow")
stats_table.add_column("Value", style="green")

stats_table.add_row("Total Reviews", str(stats['total_reviews']))
stats_table.add_row("Average Rating", f"{stats['avg_rating']:.2f} ⭐")
stats_table.add_row("Restaurants", str(stats['restaurants']))

console.print(stats_table)

conn.close()
