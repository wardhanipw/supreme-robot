Database setup
--------------

This workspace includes SQL files to create a `restaurant_reviews` database and two tables: `restaurant` and `review`.

Files added:
- [db/postgres_schema.sql](db/postgres_schema.sql) - PostgreSQL schema and instructions.
- [db/sqlite_schema.sql](db/sqlite_schema.sql) - SQLite schema (uses foreign keys pragma).
- [db/seed.sql](db/seed.sql) - Sample seed data.

Quick commands

SQLite (quick test):
```
sqlite3 restaurant_reviews.db < db/sqlite_schema.sql
sqlite3 restaurant_reviews.db < db/seed.sql
sqlite3 restaurant_reviews.db "SELECT * FROM restaurant;"
```

PostgreSQL (recommended for production-like behavior):
```
psql -c "CREATE DATABASE restaurant_reviews;"
psql -d restaurant_reviews -f db/postgres_schema.sql
psql -d restaurant_reviews -f db/seed.sql
```

If you need help running these commands or want a small script to automate this, tell me and I will add one.

Running the SQLite scripts
--------------------------

1. Initialize the database and seed sample data:
```bash
bash scripts/init_sqlite.sh
```

2. View restaurants and reviews in JSON:
```bash
python3 scripts/show_reviews_json.py
```

3. View each restaurant with its menu and average rating in JSON:
```bash
python3 scripts/menu_with_avg.py
```

4. Export the combined restaurant/menu data to CSV:
```bash
python3 scripts/menu_with_avg_csv.py
```

5. Export separate CSV files for restaurants and menu items:
```bash
python3 scripts/export_separate_csvs.py
```

Result files
------------

- `output/show_reviews.json`
- `output/restaurants_with_menu.json`
- `output/restaurants_with_menu.csv`
- `output/restaurants.csv`
- `output/menu.csv`

If you want, I can also add a single wrapper script such as `scripts/run_all.sh` to run everything in one command.
# supreme-robot