#nama = Muhamad Fikri Alafahrezi  
#kelas =  XI-TKJ 2
#no = 19

#Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan
#dengan eksponen tertentu.

def hitung_pangkat(bilangan, eksponen):
    hasil = bilangan ** eksponen
    return hasil


bilangan = float(input("Masukkan bilangan: "))  
eksponen = int(input("Masukkan eksponen (bilangan bulat): "))

hasil_pangkat = hitung_pangkat(bilangan, eksponen)
print(f"{bilangan} pangkat {eksponen} adalah {hasil_pangkat}.")