# Nama    :Muhamad Fikri Alfahrezi
# Kelas   :XI-TKJ2
# No      :19
# Soal    :Seorang petani memiliki 100 ekor ayam di peternakannnya. setiap  bulan, jumlah
#          bertambah 5% dari jumlah ayam pada bulan sebelumnya. Buatlah program yang menghitung
#          berapa bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor

bulan = 0
jumlah_ayam = 100
while jumlah_ayam < 200:
    bulan += 1
    pertambahan_ayam = jumlah_ayam * 0.05
    jumlah_ayam = jumlah_ayam + pertambahan_ayam
    print("membutuhkan", bulan, "bulan untuk", jumlah_ayam, "ayam")