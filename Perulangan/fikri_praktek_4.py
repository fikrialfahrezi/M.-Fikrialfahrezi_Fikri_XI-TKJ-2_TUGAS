# Nama    :Muhamad Fikri Alfahrezi
# Kelas   :XI-TKJ2
# No      :19
# Soal    :Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari
#          jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisa
#          apel kurang dari 20 buah.

jumlah_apel_awal = 100
batas_apel = 20
persentase_penjualan = 0.10

hari = 0

while jumlah_apel_awal > batas_apel:
    jumlah_apel_terjual = jumlah_apel_awal * persentase_penjualan
    jumlah_apel_awal -= jumlah_apel_terjual
    hari += 1

print(f"Dibutuhkan {hari} hari agar sisa apel kurang dari {batas_apel} buah.")