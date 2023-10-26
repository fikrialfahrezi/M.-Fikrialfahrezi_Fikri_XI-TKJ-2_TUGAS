# nama: Muhamad fikri
# kelas: XI 2
# nomor absen: 19 
# soal: Buat program Python yang mengambil total belanjaan dan status anggota (biasa atau premium).Berikan diskon berdasarkan aturan berikut:
# - Anggota premium: Jika total belanjaan lebih dari 500.000, berikan diskon 15%. Jika tidak,berikan diskon 10%.
# - Anggota biasa: Jika total belanjaan lebih dari 300.000, berikan diskon 7%. Jika tidak, berikan

total_belanjaan = float(input("Masukkan total belanjaan: "))
status_anggota = input("Masukkan status anggota (biasa/premium): ").lower()
diskon = 0

if status_anggota == "premium":
    if total_belanjaan > 500000:
        diskon = 0.15  # 15% diskon untuk anggota premium jika total belanjaan > 500.000
    else:
        diskon = 0.10  # 10% diskon untuk anggota premium jika total belanjaan <= 500.000
elif status_anggota == "biasa":
    if total_belanjaan > 300000:
        diskon = 0.07  # 7% diskon untuk anggota biasa jika total belanjaan > 300.000

jumlah_bayar = total_belanjaan - (total_belanjaan * diskon)

print("jumlah yang harus dibayar: RP", jumlah_bayar)
