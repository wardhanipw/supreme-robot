# 📊 Opsi Tampilan Data Reviews & Menu

Kami telah membuat beberapa script Python untuk menampilkan data dari database dalam format tabel yang cantik dengan border dan styling di terminal. Semua script menggunakan library **`rich`** untuk formatting.

## ⚡ Quick Start

Install dependency:
```bash
pip install rich
```

Kemudian pilih script yang Anda inginkan dari opsi di bawah.

---

## 📋 Script yang Tersedia

### 1️⃣ **show_reviews_table.py** - Tampilan Standard
Menampilkan semua data restaurants dan reviews dalam dua tabel terpisah.

```bash
python3 scripts/show_reviews_table.py
```

**Menampilkan:**
- ✅ Tabel Restaurants (ID, Name, Address, Description)
- ✅ Tabel Reviews dengan rating bintang (⭐)
- ✅ Format: Border rounded dengan warna-warna

---

### 2️⃣ **show_reviews_advanced.py** - Berbagai Format Border
Tampilkan reviews dengan pilihan gaya border sesuai preferensi.

```bash
python3 scripts/show_reviews_advanced.py [format]
```

**Format yang tersedia:**
```bash
python3 scripts/show_reviews_advanced.py rich     # ╭─ Border rounded (default)
python3 scripts/show_reviews_advanced.py double   # ╔═ Border double line
python3 scripts/show_reviews_advanced.py heavy    # ┏━ Border tebal
python3 scripts/show_reviews_advanced.py simple   # ├─ Border simple
python3 scripts/show_reviews_advanced.py minimal  # ├─ Minimal (hanya horizontal)
```

**Bonus:**
- 📊 Statistik reviews (Total, Average Rating, Jumlah Restaurant)
- 📅 Sorted by date (terbaru dulu)

---

### 3️⃣ **show_reviews_by_restaurant.py** - Filter per Restaurant
Lihat reviews untuk restaurant spesifik dengan statistik detail.

```bash
# Lihat daftar semua restaurant
python3 scripts/show_reviews_by_restaurant.py

# Filter by nama
python3 scripts/show_reviews_by_restaurant.py "Warung"
python3 scripts/show_reviews_by_restaurant.py "Cafe"

# Filter by ID
python3 scripts/show_reviews_by_restaurant.py 1
```

**Menampilkan:**
- ✅ Reviews untuk restaurant yang dipilih
- ✅ Statistik: Total Reviews, Avg/Min/Max Rating
- ✅ Format: Border rounded dengan sorting date

---

### 4️⃣ **show_menu_table.py** - Menu dengan Rating
Tampilkan semua menu dari setiap restaurant dengan average rating.

```bash
python3 scripts/show_menu_table.py
```

**Menampilkan:**
- ✅ Item menu untuk setiap restaurant
- ✅ Harga (Rp)
- ✅ Deskripsi item
- ✅ Average rating restaurant (⭐)

---

## 🎨 Format Comparison

Lihat perbedaan visual antara format yang tersedia:

### **RICH (Rounded)**
```
╭──────┬───────────╮
│ Col1 │ Col2      │
├──────┼───────────┤
│ Val1 │ Value 2   │
╰──────┴───────────╯
```

### **DOUBLE (Double Line)**
```
╔══════╦═══════════╗
║ Col1 ║ Col2      ║
╠══════╬═══════════╣
║ Val1 ║ Value 2   ║
╚══════╩═══════════╝
```

### **HEAVY (Bold)**
```
┏━━━━━━┳━━━━━━━━━━━┓
┃ Col1 ┃ Col2      ┃
┣━━━━━━╋━━━━━━━━━━━┫
┃ Val1 ┃ Value 2   ┃
┗━━━━━━┻━━━━━━━━━━━┛
```

### **SIMPLE**
```
  Col1  Col2
  Val1  Value 2
```

---

## 💡 Tips & Tricks

### Membuat Alias (Opsional)
Tambahkan ke `~/.bashrc` atau `~/.zshrc`:

```bash
alias reviews="python3 scripts/show_reviews_table.py"
alias reviews-adv="python3 scripts/show_reviews_advanced.py"
alias reviews-rest="python3 scripts/show_reviews_by_restaurant.py"
alias menu="python3 scripts/show_menu_table.py"
```

Kemudian gunakan langsung:
```bash
reviews
reviews-adv double
reviews-rest "Warung"
menu
```

### Query Langsung via SQLite
Jika ingin query langsung tanpa Python:

```bash
# Tampil semua reviews dengan nama restaurant
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

---

## 📁 File Struktur

```
scripts/
├── show_reviews_table.py          # ✅ Standard display
├── show_reviews_advanced.py       # ✅ Multiple formats
├── show_reviews_by_restaurant.py  # ✅ Filter by restaurant
├── show_menu_table.py             # ✅ Menu with ratings
├── show_reviews_json.py           # (existing) JSON output
├── show_reviews.py                # (existing) Plain text output
└── menu_with_avg.py               # (existing) JSON menu
```

---

## ✅ Checklist Penggunaan

- [ ] Install `rich`: `pip install rich`
- [ ] Jalankan `bash scripts/init_sqlite.sh` untuk setup database
- [ ] Pilih script sesuai kebutuhan
- [ ] Coba berbagai format untuk melihat mana yang paling bagus
- [ ] Buat alias untuk akses cepat (opsional)

---

## 🤔 Pertanyaan Umum

**Q: Perintah mana yang harus saya gunakan untuk viewing standar?**  
A: Gunakan `show_reviews_table.py` - ini paling lengkap dan informatif.

**Q: Saya ingin tampilan yang lebih "mewah"?**  
A: Coba `show_reviews_advanced.py double` atau `heavy` untuk tampilan lebih profesional.

**Q: Bagaimana cara lihat reviews untuk restaurant tertentu?**  
A: Gunakan `show_reviews_by_restaurant.py` dan search by nama atau ID.

**Q: Apa itu library `rich`?**  
A: Library Python untuk formatting text dan tabel di terminal dengan styling warna dan border yang cantik.

---

Enjoy! 🎉

