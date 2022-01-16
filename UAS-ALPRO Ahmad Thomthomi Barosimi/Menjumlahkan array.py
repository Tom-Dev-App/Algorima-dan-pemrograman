print("##################")
print("Menjumlahkan array") #judul
print("##################")
array1 = {1, 2, 3} #Bilangan array 1
array2 = {4, 5, 6} #Bilangan array 2

collectData = zip(array1, array2) #Menggabungkan data ke-2 array

result = [x+y for (x,y) in collectData] #Menjulahkan ke-2 array
print("Hasil penjumlahan sesuai indeks dalam array ", result) #Tampilkan hasil