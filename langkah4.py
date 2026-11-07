# 6. UPDATE VARIABEL DINAMIS
daftar_matkul = ["Algoritma dan Pemrograman", "Sistem Digital", "Arsitektur dan Organisasi Komputer"]
transkrip_nilai = {
    "Algoritma dan Pemrograman": 4.0,
    "Sistem Digital": 3.0,
    "Arsitektur dan Organisasi Komputer": 4.0
}
total_nilai = 85.5 + 78.0 + 90.2

matkul_baru = "Jaringan Komputer"
nilai_matkul_baru_str = "88.0"
mutu_matkul_baru = 3.5

# A. Tambahkan ke List
daftar_matkul.append(matkul_baru)

# B. Tambahkan ke Dictionary
transkrip_nilai[matkul_baru] = mutu_matkul_baru

# C. Rekalkulasi Variabel Total & Rata-rata
nilai_jk = float(nilai_matkul_baru_str)
total_nilai = total_nilai + nilai_jk
jumlah_matkul = len(daftar_matkul)
rata_rata_terbaru = total_nilai / jumlah_matkul

# D. Hitung Indeks Prestasi Kumulatif (IPK)
total_bobot_mutu = sum(transkrip_nilai.values())
ipk_sementara = total_bobot_mutu / jumlah_matkul

print("\n--- HASIL REKALKULASI SETELAH PENAMBAHAN MATKUL ---")
print("Daftar Matkul Terbaru     :", daftar_matkul)
print("Jumlah Matkul Total       :", jumlah_matkul)
print("Rata-Rata Angka Baru      :", round(rata_rata_terbaru, 2))
print("IPK Sementara (Skala 4)   :", round(ipk_sementara, 2))