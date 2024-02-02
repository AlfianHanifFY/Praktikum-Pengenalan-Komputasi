#Nama/NIM : Alfian Hanif Fitria Yustanto/19623281
#Tanggal : 21 September 2023
#Deskripsi : Program menghitung rangkaian resistor

#kamus
#r1 = integer
#r2 = integer
#r3 = integer
#r_total = float

#algoritma

#input
r1 = int(input("Masukkan nilai resistor Pertama : "))
r2 = int(input("Masukkan nilai resistor kedua : "))
r3 = int(input("Masukkan nilai resistor ketiga : "))

#proses
if(r1 > 0 and r2>0 and r3>0):
  r_total = float((r1/10) + (r2/10) + (r3/10))
  print("Total hambatan rangkaian adalaj",str(r_total),"ohm.")
else: #ada nilai r<0
  print("Tidak dapat menghitung hambatan.")