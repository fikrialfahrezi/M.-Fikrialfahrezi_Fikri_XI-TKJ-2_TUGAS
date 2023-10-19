# nama: 
# kelas:
# nomor absen:
# soal: Buat program Python yang mengambil status persiapan proyek dan menentukan apakah proyektersebut dapat diluncurkan. Jika status persiapan "Siap," program harus mencetak "Proyekdiluncurkan." Jika status persiapan "Tunda," program harus mencetak "Proyek ditunda."

status_persiapan = input("Masukkan status persiapan proyek (Siap/Tunda): ").strip().lower()

# Periksa status persiapan dan tentukan hasil
if status_persiapan == "siap":
    print("Proyek diluncurkan.")
elif status_persiapan == "tunda":
    print("Proyek ditunda.")
else:
    print("Status persiapan tidak valid. Harap masukkan 'Siap' atau 'Tunda'.")