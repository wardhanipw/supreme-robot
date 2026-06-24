#!/usr/bin/env bash
set -euo pipefail

DB=restaurant_reviews.db
echo "Creating SQLite DB: $DB"
rm -f "$DB"

sqlite3 "$DB" < db/sqlite_schema.sql
sqlite3 "$DB" < db/seed.sql

echo "Database created and seeded: $DB"
echo
echo "Restaurants:"
sqlite3 -header -column "$DB" "SELECT id, name, street_address FROM restaurant;"
