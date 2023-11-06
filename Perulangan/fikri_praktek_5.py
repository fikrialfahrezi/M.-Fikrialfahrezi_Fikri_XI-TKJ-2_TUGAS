# Nama    :Muhamad Fikri Alfahrezi
# Kelas   :XI-TKJ2
# No      :19
# Soal    :Sebuah bakteri pembelahan setiap 20 menit. Sebuah bakteri ditempatkan dalam lingkungan yang cocok dan berkembang biak dengan cepat. Buatlah program yang
#          menghitung berapa kali pembelahan bakteri terjadi dalam rentang waktu 2 jam.

interval_pembelahan = 20
total_waktu = 120

jumlah_pembelahan = 0

while total_waktu >= interval_pembelahan:
    total_waktu -= interval_pembelahan
    jumlah_pembelahan += 1

print(
    f"Pembelahan bakteri terjadi sebanyak {jumlah_pembelahan} kali dalam rentang waktu 2 jam."
)