print("#########################")
print("Program Bilangan Terbesar") #Judul program
print("#########################")
myList = [] #list untuk menampung semua data
for i in range(1, 4): #Loop menginputkan 3 kali
    numbers = int(input("Masukkan angka : ")) #Var numbers untuk menampung data semesntara
    myList.append(numbers) #Mengisi nilai dari var numbers ke list
maxNumber = max(myList) #Bilangan terbesar yang diinputkan
print("Angka terbesar yang anda inputkan adalah : ", maxNumber) #Menampilkan bilangan terbesar