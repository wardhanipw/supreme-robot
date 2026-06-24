-- Sample seed data for restaurant_reviews

INSERT INTO restaurant (name, street_address, description) VALUES
('Warung Makan Bintang', 'Jl. Sudirman 12', 'Masakan Indonesia otentik'),
('Cafe Kopi Kita', 'Jl. Melati 5', 'Kopi spesial dan dessert'),
('Nasi Goreng Asli', 'Jl. Kenanga 3', 'Nasi goreng tradisional dengan resep keluarga');

INSERT INTO review (restaurant_id, user_name, rating, review_text, review_date) VALUES
(1, 'Andi', 5, 'Makanannya enak dan harga terjangkau', '2024-05-10'),
(1, 'Siti', 4, 'Pelayanan ramah, porsi cukup', '2024-06-01'),
(2, 'Budi', 5, 'Kopi terbaik di kota', '2024-06-15'),
(2, 'Citra', 4, 'Suasana nyaman, cocok untuk ngobrol', '2024-06-20'),
(3, 'Dedi', 5, 'Nasi goreng terenak yang pernah saya coba', '2024-06-21');

-- Menu items: at least 3 per restaurant
INSERT INTO menu (restaurant_id, name, price, description) VALUES
(1, 'Ayam Goreng Bumbu', 25000, 'Ayam goreng spesial dengan sambal'),
(1, 'Sate Lilit', 30000, 'Sate ikan khas Bali'),
(1, 'Es Teh Manis', 8000, 'Minuman penyegar'),

(2, 'Espresso', 18000, 'Kopi single shot'),
(2, 'Cappuccino', 25000, 'Kopi dengan steamed milk'),
(2, 'Croissant', 15000, 'Pastry mentega'),

(3, 'Nasi Goreng Special', 22000, 'Nasi goreng dengan telur dan ayam'),
(3, 'Nasi Goreng Seafood', 28000, 'Nasi goreng dengan udang dan cumi'),
(3, 'Kerupuk', 5000, 'Pelengkap nasi goreng');
