# Summary - Semua Script yang Telah Dibuat

## 📊 Script Reporting & Query

Terdapat 6 script Python baru untuk menampilkan data restaurants dan reviews dalam format tabel yang cantik dengan border.

### Prerequisites
Install library `rich` terlebih dahulu:
```bash
pip install rich
```

---

## 📋 Daftar Script

### 1. **show_reviews_table.py** - Standard Display
Menampilkan semua restaurants dan reviews dalam dua tabel terpisah.

**Command:**
```bash
python3 scripts/show_reviews_table.py
```

**Output:**
- Tabel Restaurants (ID, Name, Address, Description)
- Tabel Reviews dengan rating bintang (⭐)

---

### 2. **show_reviews_advanced.py** - Multiple Format Styles
Menampilkan reviews dengan pilihan format border yang berbeda.

**Command:**
```bash
python3 scripts/show_reviews_advanced.py [format]
```

**Available Formats:**
- `rich` - Border rounded (default)
- `double` - Border double line (╔═)
- `heavy` - Border tebal (┏━)
- `simple` - Border simple
- `minimal` - Minimal (hanya horizontal)

**Example:**
```bash
python3 scripts/show_reviews_advanced.py double
python3 scripts/show_reviews_advanced.py heavy
```

**Bonus Features:**
- Statistik reviews (Total, Average Rating, Jumlah Restaurant)
- Sorted by date (terbaru dulu)

---

### 3. **show_reviews_by_restaurant.py** - Filter by Restaurant
Menampilkan reviews untuk restaurant tertentu dengan statistik detail.

**Command:**
```bash
# Lihat daftar restaurant
python3 scripts/show_reviews_by_restaurant.py

# Filter by nama
python3 scripts/show_reviews_by_restaurant.py "Warung"
python3 scripts/show_reviews_by_restaurant.py "Cafe"

# Filter by ID
python3 scripts/show_reviews_by_restaurant.py 1
```

**Output:**
- Reviews untuk restaurant yang dipilih
- Statistik: Total Reviews, Avg/Min/Max Rating
- Sorted by date

---

### 4. **show_menu_table.py** - Menu dengan Rating
Menampilkan menu dari setiap restaurant dengan average rating.

**Command:**
```bash
python3 scripts/show_menu_table.py
```

**Output:**
- Item menu untuk setiap restaurant
- Harga (Rp)
- Deskripsi item
- Average rating restaurant (⭐)

---

## 🔍 Additional Queries Scripts

### 5. **additional_queries.py** - 3 Main Queries
Script yang menampilkan hasil dari 3 additional queries:

**Command:**
```bash
python3 scripts/additional_queries.py
```

**Queries yang ditampilkan:**

**Query 1: Highest-Rated Restaurant**
```
Find the highest-rated restaurant based on average rating of all its reviews
```
Output: Restaurant dengan rating tertinggi

**Query 2: Number of Reviews per Restaurant**
```
Find the number of reviews each restaurant has received
```
Output: Tabel berisi jumlah reviews untuk setiap restaurant (sorted by total reviews DESC)

**Query 3: Most Recent Review for Each Restaurant**
```
Display the most recent review for each restaurant
```
Output: Review terbaru untuk setiap restaurant dengan user, rating, text, dan date

---

### 6. **restaurant_menu_rating.py** - Restaurant Menu with Rating
Menampilkan setiap restaurant dengan menu dan average rating dari reviews.

**Command:**
```bash
python3 scripts/restaurant_menu_rating.py
```

**Output:**
- Untuk setiap restaurant:
  - Nama restaurant
  - Average rating (⭐)
  - Jumlah reviews
  - Daftar menu (Item, Price, Description)

---

## 📁 Complete File Structure

```
scripts/
├── show_reviews_table.py           # ✅ Standard display
├── show_reviews_advanced.py        # ✅ Multiple format styles
├── show_reviews_by_restaurant.py   # ✅ Filter by restaurant
├── show_menu_table.py              # ✅ Menu with ratings
├── additional_queries.py           # ✅ 3 Additional queries
├── restaurant_menu_rating.py       # ✅ Restaurant menu + rating
├── show_reviews_json.py            # (existing) JSON output
├── show_reviews.py                 # (existing) Plain text
└── menu_with_avg.py                # (existing) JSON menu
```

---

## 🚀 Quick Reference

| Purpose | Command |
|---------|---------|
| View semua data | `python3 scripts/show_reviews_table.py` |
| Format berbeda | `python3 scripts/show_reviews_advanced.py double` |
| Filter restaurant | `python3 scripts/show_reviews_by_restaurant.py "Nama"` |
| Menu dengan rating | `python3 scripts/show_menu_table.py` |
| Query-query tambahan | `python3 scripts/additional_queries.py` |
| Restaurant + Menu + Rating | `python3 scripts/restaurant_menu_rating.py` |

---

## 💡 Tips

### Membuat Alias (Opsional)
Tambahkan ke `~/.bashrc` atau `~/.zshrc`:

```bash
alias reviews="python3 scripts/show_reviews_table.py"
alias reviews-adv="python3 scripts/show_reviews_advanced.py"
alias reviews-rest="python3 scripts/show_reviews_by_restaurant.py"
alias menu="python3 scripts/show_menu_table.py"
alias queries="python3 scripts/additional_queries.py"
alias menu-rating="python3 scripts/restaurant_menu_rating.py"
```

Penggunaan:
```bash
reviews
reviews-adv double
reviews-rest "Cafe"
menu
queries
menu-rating
```

---

## 📌 Database Info

Database: `restaurant_reviews.db`

**Tables:**
- `restaurant` - Informasi restaurant
- `review` - Review dari customers
- `menu` - Menu items

**Sample Data:**
- 3 restaurants
- 5 reviews
- 9 menu items

---

Semua script sudah siap digunakan! 🎉
