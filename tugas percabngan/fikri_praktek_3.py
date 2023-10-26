# nama:
# kelas:
# nomor absen:
# soal: Buat program Python yang memeriksa apakah suatu file sudah ada di direktori server. Jika file sudah ada, program harus mencetak "File sudah ada," jika tidak, program harus mencetak "File belum ada"

nama_file = "data.txt"
daftar_file_di_server = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

if nama_file in daftar_file_di_server:
    print("file sudah ada")
else:
    print("file belum ada")