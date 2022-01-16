print("################################") # Hanya judul saat program run
print("Program jumlah angka yang muncul")
print("################################")
mylist = [] #membuat variabel mylist dalam bentuk list untuk menampung data yang akan diinputkan
for i in range(1, 10): #Membuat jangkauan berapa kali nilai diinputkan
    data = int(input("Masukkan angka : ")) #Variabel data akan menampung data yang diinputkan
    mylist.append(data) #Kemudian dari variabel data dimasukkan ke variabel mylist
X = int(input("Masukkan angka yang dicari : ")) #Menginputkan berapa nilai yang muncul dari nilai yg diinputkan
print("Angka", X, "muncul sebanyak",mylist.count(X), "kali") #Menampilkan seberapa banyak angka yang diinputkan oleh user
print(mylist) #Menampilkan semua data yang diinputkan