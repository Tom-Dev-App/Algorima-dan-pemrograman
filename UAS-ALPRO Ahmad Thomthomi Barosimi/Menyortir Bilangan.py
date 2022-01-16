print("#########################")
print("Program mengurutkan angka") #Judul program
print("#########################")
numbers = [] #List menampung data inputan

for i in range(1, 4): #Ualngi memasukkan data 3 kali
    data = int(input("Masukkan bilangan bulat : ")) #Memasukkan data ke var data
    numbers.append(data) #Memasukkan dari var data ke list numbers
print("Bilangan yang anda masukkan : ", numbers) #Menampilkan data tidak tersortir
numbers.sort() #Mensortir dari kecil ke besar
print("Mengurutkan angka dari yang terkecil : ", numbers) #Menampilkan data yang disortir