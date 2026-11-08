# 3. KONVERSI TIPE DATA (Type Casting)
str_nilai_algoritma = "87.7"
str_nilai_basis_data = "77.7"
str_nilai_pemrograman_web = "89.7"

is_aktif = True
sks_per_matkul = 4

nilai_algo = float(str_nilai_algoritma)
nilai_bd = float(str_nilai_basis_data)
nilai_web = float(str_nilai_pemrograman_web)

# 4. KALKULASI MENGGUNAKAN VARIABEL
total_nilai = nilai_algo + nilai_bd + nilai_web
jumlah_matkul = 6
rata_rata_nilai = total_nilai / jumlah_matkul
total_sks_diambil = jumlah_matkul * sks_per_matkul

# Penentuan status kelulusan semester (Boolean)
is_lulus_semester = (rata_rata_nilai >= 70.0) and is_aktif

print("\n--- HASIL EVALUASI AWAL ---")
print("Total Nilai         :", total_nilai)
print("Rata-Rata Nilai     :", round(rata_rata_nilai, 2))
print("Total SKS           :", total_sks_diambil)
print("Status Lulus        :", is_lulus_semester)
