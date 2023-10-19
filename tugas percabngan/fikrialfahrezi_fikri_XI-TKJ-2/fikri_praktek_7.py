# nama: Muhmad fikri
# kelas: XI 2
# nomor absen: 19
# soal: Buat program Python yang mengambil informasi pembaruan perangkat lunak dan menentukanapakah sistem perlu di-restart. Jika pembaruan mengharuskan restart, program harus mencetak "Sistem perlu di-restart." Jika tidak, program harus mencetak "Sistem tidak perlu di-restart."

perlu_restart = (input("apakah pc atau laptop anda perlu di restart? (iya/tidak): "))

if perlu_restart.lower() == "iya":
    print("pc atau laptop di-restart.")
else:
    print("pc atau laptop tidak perlu di-restart.")
