# nama: Muamad fikri
# kelas: XI 2
# nomor absen: 19 
# soal: Buat program Python yang mengambil data penjualan bulanan produk dan menentukan kategoriproduk berdasarkan penjualan:
# - Jika penjualan lebih dari 1000 unit, kategorikan sebagai "Produk Terlaris."
# - Jika penjualan antara 500 hingga 1000 unit, kategorikan sebagai "Produk Populer."
# - Jika penjualan kurang dari 500 unit, kategorikan sebagai "Produk Biasa."

# Mengambil data penjiulan bulanan produk dari pengguna
penjualan = int(input("Masukkan jumlah penjualan bulanan produk: "))

# Menentukan kategori produk berdasarkan penjualan
if penjualan > 1000:
   kategori = "Produk Terlsris"
elif 500 <= penjualan <= 1000:
    kategori = "Produk Populer"
else:
    kategori = "Produk Biasa"

# Mencetak hasil
print("Jumlah Penjualan Bulanan:", penjualan, "unit")
print("Kategori Produk:", kategori)

