#nama = Muhamad Fikri Alfarezi
#kelas =  XI-TKJ 2
#no = 19

#Deskripsi Pekerjaan: Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.

def faktorial(n):
    if n == 0:
        return 1  
    else:
        hasil = 1
        for i in range(1, n + 1):
            hasil *= i
        return hasil

bilangan = int(input("Masukkan bilangan: "))
hasil_faktorial = faktorial(bilangan)
print(f"Faktorial dari {bilangan} adalah {hasil_faktorial}.")