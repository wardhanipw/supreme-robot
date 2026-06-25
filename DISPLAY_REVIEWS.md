### 1. **show_reviews_table.py** - Tabel Standar

Menampilkan semua restaurants dan reviews dalam dua tabel terpisah dengan format standar.

**Penggunaan:**
```bash
python3 scripts/show_reviews_table.py
```

**Fitur:**
- Menampilkan tabel Restaurants (ID, Name, Address, Description)
- Menampilkan tabel Reviews dengan bintang rating (⭐)
- Reviews ditampilkan dengan warna-warna yang berbeda
- Border bulat (rounded)

**Output Contoh:**
```
RESTAURANTS
┏━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━┓
┃ ID ┃ Name   ┃ Address┃ Desc   ┃
┣━━━━╋━━━━━━━━╋━━━━━━━━╋━━━━━━━━┫
│ 1  │ Warung │ Jl.123 │ Masakan│
└────┴────────┴────────┴────────┘
```

### 2. **show_reviews_advanced.py** - Tabel dengan Berbagai Format

Menampilkan reviews dalam berbagai style format border. Cocok untuk memilih styling yang Anda sukai.

**Penggunaan:**
```bash
python3 scripts/show_reviews_advanced.py [format]
```

**Format yang Tersedia:**
- `rich` - Border rounded (default)
- `simple` - Border sederhana
- `double` - Border dengan garis double
- `heavy` - Border tebal
- `minimal` - Hanya garis horizontal

**Contoh:**
```bash
python3 scripts/show_reviews_advanced.py rich      # Border rounded
python3 scripts/show_reviews_advanced.py double    # Border double
python3 scripts/show_reviews_advanced.py heavy     # Border tebal
```

**Fitur Tambahan:**
- Menampilkan statistik reviews (Total, Average Rating, Jumlah Restaurant)
- Sorted by date (terbaru dulu)

### 3. **show_reviews_by_restaurant.py** - Filter Reviews per Restaurant

Menampilkan reviews untuk restaurant tertentu dengan statistik lengkap.

**Penggunaan:**
```bash
# Lihat daftar restaurant
python3 scripts/show_reviews_by_restaurant.py

# Filter by nama restaurant
python3 scripts/show_reviews_by_restaurant.py "Warung Makan"
python3 scripts/show_reviews_by_restaurant.py "Cafe Kopi"

# Filter by ID
python3 scripts/show_reviews_by_restaurant.py 1
```

**Fitur:**
- Otomatis mencari restaurant by name atau ID
- Menampilkan semua reviews untuk restaurant yang dipilih
- Statistik per restaurant:
  - Total Reviews
  - Average Rating dengan bintang
  - Min & Max Rating
- Sorted by date (terbaru dulu)

**Contoh Output:**
```
Reviews for: Warung Makan Bintang
╭───────┬──────────────┬──────────────┬─────────────────────┬──────────────╮
│ ID    │ User         │ Rating       │ Review              │ Date         │
├───────┼──────────────┼──────────────┼─────────────────────┼──────────────┤
│ 2     │ Siti         │ ⭐⭐⭐⭐     │ Pelayanan ramah     │ 2024-06-01   │
│       │              │ (4/5)        │                     │              │
│ 1     │ Andi         │ ⭐⭐⭐⭐⭐   │ Enak & terjangkau   │ 2024-05-10   │
│       │              │ (5/5)        │                     │              │
╰───────┴──────────────┴──────────────┴─────────────────────┴──────────────╯

Restaurant Statistics:
╭────────────────┬──────────────────╮
│ Metric         │ Value            │
├────────────────┼──────────────────┤
│ Total Reviews  │ 2                │
│ Average Rating │ ⭐⭐⭐⭐ (4.50/5)│
│ Min Rating     │ ⭐⭐⭐⭐ (4/5)   │
│ Max Rating     │ ⭐⭐⭐⭐⭐ (5/5) │
╰────────────────┴──────────────────╯
```

## Format Border Comparison

### Rich (Rounded)
```
╭─────┬─────╮
│ Col1│ Col2│
├─────┼─────┤
│ Val1│ Val2│
╰─────┴─────╯
```

### Double
```
╔═════╦═════╗
║ Col1║ Col2║
╠═════╬═════╣
║ Val1║ Val2║
╚═════╩═════╝
```

### Heavy
```
┏━━━━━┳━━━━━┓
┃ Col1┃ Col2┃
┣━━━━━╋━━━━━┫
┃ Val1┃ Val2┃
┗━━━━━┻━━━━━┛
```

### Simple
```
  Col1  Col2
  Val1  Val2
```

## Tips Penggunaan

1. **Untuk viewing umum:** Gunakan `show_reviews_table.py` untuk melihat semua data
2. **Untuk presentasi:** Gunakan format `double` atau `heavy` untuk tampilan lebih profesional
3. **Untuk analisis restaurant spesifik:** Gunakan `show_reviews_by_restaurant.py`
4. **Untuk memilih styling:** Coba berbagai format dengan `show_reviews_advanced.py`

## Membuat Alias (Opsional)

Tambahkan ke `.bashrc` atau `.zshrc` untuk membuat shortcut:

```bash
alias show-reviews="python3 scripts/show_reviews_table.py"
alias show-reviews-adv="python3 scripts/show_reviews_advanced.py"
alias show-reviews-rest="python3 scripts/show_reviews_by_restaurant.py"
```

Kemudian gunakan:
```bash
show-reviews
show-reviews-adv double
show-reviews-rest "Warung"
```

## Database Query Langsung

Jika ingin query langsung tanpa script Python, gunakan SQLite:

```bash
# Lihat semua reviews dengan restaurant name
sqlite3 restaurant_reviews.db "
SELECT 
    r.id, 
    rest.name as restaurant, 
    r.user_name, 
    r.rating, 
    r.review_text, 
    r.review_date
FROM review r
JOIN restaurant rest ON r.restaurant_id = rest.id
ORDER BY r.review_date DESC;
"
```

Atau dengan header:
```bash
sqlite3 -header -column restaurant_reviews.db "
SELECT 
    r.id, 
    rest.name as restaurant, 
    r.user_name, 
    r.rating || '/5' as rating, 
    r.review_text, 
    r.review_date
FROM review r
JOIN restaurant rest ON r.restaurant_id = rest.id
ORDER BY r.review_date DESC;
"
```
