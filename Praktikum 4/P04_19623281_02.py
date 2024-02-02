#NIM / Nama : 19623281/Alfian Hanif Fitria Yustanto
#Tanggal    : 2 November 2023
#Deskripsi  : Program menentukan suatu bom meledak atau tidak berdasarkan letak penawar bom

#Kamus
#ukuran = integer
#x_bom = integer
#y_bom = integer
#x_pen = integer
#y_pen = integer
#meledak = boolean
#peta = matrix of character

#Algoritma

#Input
ukuran = int(input("Masukkan ukuran kota : "))
x_bom = int(input("Koordinat x bom : "))
y_bom = int(input("Koordinat y bom : "))
x_pen = int(input("Koordinat x penawar : "))
y_pen = int(input("Koordinat y penawar : "))
meledak = False
#membuat matrix peta kota
peta = [["." for i in range(ukuran)] for i in range(ukuran)]

#Proses

for i in range(ukuran):
  for j in range(ukuran):
    #mencari letak bom
    if i == y_bom-1 and j == x_bom-1:
      peta[i][j] = "B"
    #memetakan efek penawar bom
    peta[i][x_pen-1] = "x"
    peta[y_pen-1][j] = "x"

#mengecek apakah bom meledak
for i in range(ukuran):
  for j in range(ukuran):
    if peta[i][j] == "B":
      meledak = True


#Output

#menampilkan peta kota
for i in range(ukuran):
  for j in range(ukuran):
    print(peta[i][j] , end=" ")
  print("")

#menampilkan kondisi bom (meledak/tidak)
if meledak :
  print("Bom akan meledak. ")
else: #meledak = False
  print("Bom tidak akan meledak. ")