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
# supreme-robot