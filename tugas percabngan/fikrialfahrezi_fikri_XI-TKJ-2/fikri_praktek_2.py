# nama: Muhamad fikri
# kelas: XI 2
# nomor absen: 19
# soal: Buat program Python yang mengambil estimasi waktu selesai proyek dan tanggal target selesai. Jikaestimasi waktu selesai lebih awal atau sama dengan tanggal target, program harus mencetak "Tepat waktu," jika tidak, program harus mencetak "Terlambat."

estimasi_selesai = input("Masukkan estimasi waktu selesai (Tahun-Bulan-Tanggal): ")
tanggal_target = input("Masukkan tanggal target selesai (Tahun-Bulan-Tanggal): ")


if estimasi_selesai <= tanggal_target:
    print("Tepat waktu")
else:
    print("Terlambat")