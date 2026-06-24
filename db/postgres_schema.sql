-- PostgreSQL schema for restaurant_reviews
-- To create and use this DB:
-- 1) Create the database (run as a superuser or with sufficient privileges):
--    CREATE DATABASE restaurant_reviews;
-- 2) Connect to it: \c restaurant_reviews
-- 3) Run the statements below.

CREATE TABLE IF NOT EXISTS restaurant (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  street_address TEXT,
  description TEXT
);

CREATE TABLE IF NOT EXISTS review (
  id SERIAL PRIMARY KEY,
  restaurant_id INTEGER NOT NULL REFERENCES restaurant(id) ON DELETE CASCADE,
  user_name TEXT,
  rating INTEGER CHECK (rating >= 1 AND rating <= 5),
  review_text TEXT,
  review_date DATE
);
