#Nama/NIM : Alfian Hanif Fitria Yustanto/19623281
#Tanggal : 21 September 2023
#Deskripsi : Program menentukan banyaknya poin yang dapat ditukarkan berdasarkan tanggal awal makan di resto 

#kamus
#awal = integer
#poin = integer
#ramen = integer
#gyoza = integer
#ocha = integer

#algoritma

#input
awal = int(input("Masukkan tanggal awal makan di resto: "))

#proses

poin = 31 - awal
if(poin>=2):
  ramen = int(poin/10)
  gyoza = int((poin%10)//5)
  ocha = int((poin%5)//2)
else:#poin<2
  ramen = 0
  gyoza = 0
  ocha = 0

#output
if(ramen>0 and gyoza >0 and ocha>0):
  print("Nona Deb mendapatkan",ramen,"Ramen,",gyoza,"Gyoza,",ocha,"Ocha.")
elif(ramen>0 and gyoza > 0 and ocha == 0):
  print("Nona Deb mendapatkan",ramen,"Ramen,",gyoza,"Gyoza.")
elif(ramen>0 and gyoza == 0 and ocha == 0):
  print("Nona Deb mendapatkan",ramen,"Ramen.")
elif(ramen==0 and gyoza >0 and ocha>0):
  print("Nona Deb mendapatkan",gyoza,"Gyoza,",ocha,"Ocha.")
elif(ramen==0 and gyoza >0 and ocha==0):
  print("Nona Deb mendapatkan",gyoza,"Gyoza.")
elif(ramen==0 and gyoza==0 and ocha>0):
  print("Nona Deb mendapatkan",ocha,"Ocha.")
else:#ramen,gyoza,ocha == 0
  print("Poin tidak cukup untuk ditukarkan.")
