# Tugas Praktikum: Sistem Profil Karakter Game RPG (B0103)

# 1. Deklarasi variabel
nama_hero = "beatrik"
level = 15
hp = 100.0
is_alive = True
inventory = ["Bom", "Sniper", "Basokka"]
atribut = {"kekuatan": 60, "kelincahan": 75}

# 2. Tampilkan seluruh informasi awal
print("=== INFORMASI KARAKTER AWAL ===")
print("Nama Hero   :", nama_hero)
print("Level       :", level)
print("HP          :", hp)
print("Status Hidup:", is_alive)
print("Inventory   :", inventory)
print("Atribut     :", atribut)

# 3. Tampilkan tipe data masing-masing variabel
print("\n=== TIPE DATA MASING-MASING VARIABEL ===")
print("Tipe nama_hero  :", type(nama_hero))
print("Tipe level      :", type(level))
print("Tipe hp         :", type(hp))
print("Tipe is_alive   :", type(is_alive))
print("Tipe inventory  :", type(inventory))
print("Tipe atribut    :", type(atribut))

# 4. Kerjakan aksi:
# - Menambahkan item "Ramuan HP"
inventory.append("Ramuan HP")

# - Karakter naik level (konversi ke float + 0.5)
level = float(level) + 0.5

# 5. Cetak kembali informasi terbaru
print("\n=== INFORMASI KARAKTER TERBARU ===")
print("Nama Hero   :", nama_hero)
print("Level Terbaru (Float):", level)
print("HP          :", hp)
print("Status Hidup:", is_alive)
print("Inventory Terbaru   :", inventory)
print("Atribut     :", atribut)
