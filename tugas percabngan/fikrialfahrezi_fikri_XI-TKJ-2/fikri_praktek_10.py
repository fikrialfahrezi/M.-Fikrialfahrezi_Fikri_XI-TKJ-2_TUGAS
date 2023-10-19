# nama: 
# kelas:
# nomor absen:
# soal: Buat program Python yang mengambil durasi peminjaman buku dalam hari dan menentukan jenis pinjaman berdasarkan aturan berikut:
# - Peminjaman 7 hari atau kurang: "Peminjaman Pendek"
# - Peminjaman lebih dari 7 hari hingga 30 hari: "Peminjaman Menengah"
# - Peminjaman lebih dari 30 hari: "Peminjaman Panjang"

durasi_peminjaman = int (input("Masukkan durasi peminjaman buku (dalam hari): "))

# Tentukan jenis pinjaman berdasarkan durasi
jenis_pinjaman = ""

if durasi_peminjaman <= 7:
    jenis_pinjaman = "Peminjaman Pendek"
elif durasi_peminjaman <= 30:
    jenis_pinjaman = "Peminjaman Menengah"
else:
    jenis_pinjaman = "Peminjaman Panjang"

# Cetak jenis pinjaman
print(f"Jenis Pinjaman: {jenis_pinjaman}")






