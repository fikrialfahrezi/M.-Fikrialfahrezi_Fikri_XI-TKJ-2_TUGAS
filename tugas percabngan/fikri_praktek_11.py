# nama: 
# kelas:
# nomor absen:
# soal: Buat program Python yang mengambil nilai performa karyawan (1 hingga 5, dengan 5 sebagaiperforma terbaik) dan menghitung bonus tahunan berdasarkan aturan berikut:
# - Performa 5: Bonus 20% dari gaji tahunan.
# - Performa 4: Bonus 10% dari gaji tahunan.
# - Performa 3: Bonus 5% dari gaji tahunan.
# - Performa 2: Bonus 2% dari gaji tahunan.
# - Performa 1: Tidak ada bonus.

performa = int(input("Masukkan nilai performa karyawan (1-5): "))

# Input gaji tahunan karyawan
gaji_tahunan = float(input("Masukkan gaji tahunan karyawan: "))

# Inisialisasi bonus
bonus = 0

# Hitung bonus berdasarkan performa
if performa == 5:
    bonus = 0.20 * gaji_tahunan  # Bonus 20% untuk performa 5
elif performa == 4:
    bonus = 0.10 * gaji_tahunan  # Bonus 10% untuk performa 4
elif performa == 3:
    bonus = 0.05 * gaji_tahunan  # Bonus 5% untuk performa 3
elif performa == 2:
    bonus = 0.02 * gaji_tahunan  # Bonus 2% untuk performa 2

# Cetak bonus tahunan
if bonus > 0:
    print(f"Bonus tahunan: Rp {bonus:.2f}")
else:
    print("Tidak ada bonus.")






