#nama/nim : Alfian Hanif Fitria Yustanto / 19623281
#tanggal : 5 Oktober 2023
#Deskripsi : Program membuat segitiga sebanyak n kali

#kamus
#n : integer
#i : integer

#algoritma

#input
n = 0
while n <= 0:
  n = int(input("Masukkan banyak segitiga : "))
a = 0
#proses
for i in range(3):
    if i == 0 :
      for j in range(5 + (n-1)*4):
        if j == a + i:
          print('*', end="")
          a += 1 + i
        else:
          print(" ", end="")
    if i == 1:
       for j in range(5 + (n-1)*4):
        if j == a:
          print(" ", end="")
          a += 4
        else:
          print("*", end="")
    if i == 2:
      for j in range(5 + (n-1)*4):
        if j == a+2:
          print("*", end="")
          a += 4
        else:
          print(" ", end="")
    a = 0
    print("")
  
  