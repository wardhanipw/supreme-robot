#!/usr/bin/env python3
"""
Additional Queries:
1. Find the highest-rated restaurant based on average rating
2. Find the number of reviews each restaurant has received
3. Display the most recent review for each restaurant
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

# ========== QUERY 1: Highest-Rated Restaurant ==========
console.print("\n[bold cyan]QUERY 1: Highest-Rated Restaurant[/bold cyan]")
console.print("[yellow]Find the highest-rated restaurant based on average rating of all its reviews[/yellow]\n")

highest_rated = cur.execute('''
    SELECT 
        r.id,
        r.name,
        COUNT(rv.id) as total_reviews,
        AVG(rv.rating) as avg_rating
    FROM restaurant r
    LEFT JOIN review rv ON r.id = rv.restaurant_id
    GROUP BY r.id
    ORDER BY avg_rating DESC
    LIMIT 1
''').fetchone()

if highest_rated:
    table1 = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    table1.add_column("Restaurant", style="green")
    table1.add_column("Avg Rating", style="cyan")
    table1.add_column("Total Reviews", style="yellow")
    
    rating_stars = "⭐" * round(highest_rated['avg_rating'])
    table1.add_row(
        highest_rated['name'],
        f"{rating_stars}\n({highest_rated['avg_rating']:.2f}/5)",
        str(highest_rated['total_reviews'])
    )
    console.print(table1)
else:
    console.print("[red]No restaurants found[/red]")

# ========== QUERY 2: Number of Reviews per Restaurant ==========
console.print("\n[bold cyan]QUERY 2: Number of Reviews per Restaurant[/bold cyan]")
console.print("[yellow]Find the number of reviews each restaurant has received[/yellow]\n")

review_counts = cur.execute('''
    SELECT 
        r.id,
        r.name,
        COUNT(rv.id) as total_reviews,
        AVG(rv.rating) as avg_rating
    FROM restaurant r
    LEFT JOIN review rv ON r.id = rv.restaurant_id
    GROUP BY r.id
    ORDER BY total_reviews DESC
''').fetchall()

table2 = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
table2.add_column("Restaurant", style="green")
table2.add_column("Total Reviews", style="cyan", width=15)
table2.add_column("Avg Rating", style="yellow")

for row in review_counts:
    rating_stars = "⭐" * round(row['avg_rating']) if row['avg_rating'] else "No ratings"
    table2.add_row(
        row['name'],
        str(row['total_reviews']),
        f"{rating_stars}\n({row['avg_rating']:.2f}/5)" if row['avg_rating'] else "N/A"
    )

console.print(table2)

# ========== QUERY 3: Most Recent Review per Restaurant ==========
console.print("\n[bold cyan]QUERY 3: Most Recent Review for Each Restaurant[/bold cyan]")
console.print("[yellow]Display the most recent review for each restaurant[/yellow]\n")

recent_reviews = cur.execute('''
    SELECT 
        r.name as restaurant,
        rv.user_name,
        rv.rating,
        rv.review_text,
        rv.review_date
    FROM restaurant r
    LEFT JOIN review rv ON r.id = rv.restaurant_id
    WHERE rv.id IN (
        SELECT id FROM review WHERE restaurant_id = r.id 
        ORDER BY review_date DESC LIMIT 1
    ) OR (SELECT COUNT(*) FROM review WHERE restaurant_id = r.id) = 0
    ORDER BY rv.review_date DESC NULLS LAST
''').fetchall()

table3 = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
table3.add_column("Restaurant", style="green")
table3.add_column("User", style="yellow")
table3.add_column("Rating", style="cyan", width=12)
table3.add_column("Latest Review", style="white")
table3.add_column("Date", style="blue")

for row in recent_reviews:
    if row['review_date']:
        rating_stars = "⭐" * row['rating']
        table3.add_row(
            row['restaurant'],
            row['user_name'] or "Anonymous",
            f"{rating_stars}\n({row['rating']}/5)",
            row['review_text'][:40] or "N/A",
            row['review_date'] or "N/A"
        )
    else:
        table3.add_row(
            row['restaurant'],
            "N/A",
            "No reviews",
            "No reviews",
            "N/A"
        )

console.print(table3)

conn.close()
