#nama/nim : Alfian Hanif Fitria Yustanto / 19623281
#deskripsi : Program menentukan mobil tuan kil berdasarkan plat nomor

#kamus
#plat : string
#jumlah : integer
#banyak : integer
#jumlahDigit : integer
#ketemu : Boolean
#array : list of character

#algoritma

#input
plat = input("Masukkan nomor plat mobil : ")
jumlah = int(input("Masukkan jumlah digit : "))
banyak = int(input("Masukkan banyak digit : "))
jumlahDigit = 0
ketemu = False

#proses
array = ["" for i in range(len(plat))]

for i in range(len(plat)): #memasukkan character pada plat ke array
  array[i] = plat[i]

for i in range(1,banyak+1,1): #mengecek jumlah digit pada plat
  jumlahDigit += int(array[i])

if jumlahDigit == jumlah:
  ketemu = True

if array[0] != "D":
  ketemu = False

#output
if ketemu:
  print("Mobil Tuan Kil ditemukan ! ")
else: #tidak ketemu
  print("Bukan mobil Tuan Kil ! ")

