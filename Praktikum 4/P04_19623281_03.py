#NIM / Nama : 19623281/Alfian Hanif Fitria Yustanto
#Tanggal    : 2 November 2023
#Deskripsi  : Program menyusun botol pada meja

#Kamus
#panjang = integer
#lebar = integer
#meja = matrix of integer
#botol = list of integer
#n = integer
#x = integer

#Algoritma

#Input
panjang = int(input("Masukkan panjang meja : "))
lebar = int(input("Masukkan lebar meja : "))
meja = [[0 for i in range(panjang)] for i in range(lebar)]
botol = [0 for i in range(panjang*lebar)]
n = 0
for i in range(panjang*lebar):
  botol[i] = int(input(f"tinggi botol ke-{i+1} : "))


#Proses

#mengurutkan elemen matrix botol dari paling pendek
for i in range(panjang*lebar-1):
  for j in range((panjang*lebar-1)):
    if botol[j] > botol[j+1]:
      x = botol[j]
      botol[j] = botol[j+1]
      botol[j+1] = x

#membuat pola

#pusat meja
meja[lebar//2][panjang//2] = botol[panjang*lebar-1]

#meja bagian atas
for i in range(panjang):
  meja[0][i] = botol[n]
  n += 1

#meja bagian pinggir kanan dan kiri
for i in range(1, lebar-1):
  for j in range(panjang):
    if j == 0 or j == panjang-1:
      meja[i][j] = botol[n]
      n += 1

#meja bagian bawah
for i in range(panjang):
  meja[lebar-1][i] = botol[n]
  n += 1

#mengisi bagian yang belum terisi
for i in range(lebar):
  for j in range(panjang):
    if meja[i][j] == 0:
      meja[i][j] = botol[n]
      n += 1

#Output
for i in range(lebar):
  for j in range(panjang):
    print(meja[i][j] , end=" ")
  print("")