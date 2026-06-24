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
