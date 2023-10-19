# nama: 
# kelas:
# nomor absen:
# soal: Buat program Python yang mengambil nilai tugas (skala 0-100) dan nilai ujian (skala 0-100) seorangsiswa dan menentukan nilai akhirnya. Jika nilai tugas lebih dari 70 dan nilai ujian lebih dari 60, siswalulus dengan nilai "Lulus". Jika tidak, siswa gagal dengan nilai "Gagal".

nilai_tugas = float(input("Masukkan nilai tugas (skala 0-100): "))
nilai_ujian = float(input("Masukkan nilai ujian (skala 0-100): "))

if nilai_tugas > 70 and nilai_ujin > 60:
    status = "Lulus"
else:
    status = "Gagal"

print("Nilai Tugas:", nilai_tugas)
print("Nilai Ujian:", nilai_ujian)
print("status:", status)