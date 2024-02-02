#nama/nim : Alfian Hanif Fitria Yustanto / 19623281
#tanggal : 5 Oktober 2023
#Deskripsi : program menjumlahkan bilangan yang dapat dibagi oleh x dan y dalam interval A dan B 

#kamus
#A : integer
#B : integer
#x : integer
#y : integer
#hasil : integer

#algoritma

#input

A = int(input("Masukkan nilai A : "))
B = int(input("Masukkan nilai B : "))
x = int(input("Masukkan nilai x : "))
y = int(input("Masukkan nilai y : "))
hasil = 0

#proses
for i in range (A,B+1,1):
  if ( i%x == 0 and i%y == 0):
     hasil += i

#output
print("Jumlah hasi yang habis dibagi " + str(x) + " dan " + str(y) + " adalah " + str(hasil) + ".")