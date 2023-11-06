# Nama    :Muhamad Fikri Alfahrezi
# Kelas   :XI-TKJ2
# No      :19
# Soal    :Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap
#          tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi
#          melebihi 20.000 dollar.


investasi_awal = 10000
target_nilai = 20000
tingkat_pertumbuhan = 0.06

tahun = 0

while investasi_awal < target_nilai:
    investasi_awal += investasi_awal * tingkat_pertumbuhan
    tahun += 1
print(f"Dibutuhkan {tahun} tahun agar nilai investasi melebihi {target_nilai} dollar.")