#nama/nim : Alfian Hanif Fitria Yustanto / 19623281
#deskripsi : Program menghitung jarak pandang berdasarkan ketinggian petak

#kamus
#N            : integer
#petak        : list of integer
#jarakPandang : list of integer
#valid        : Boolean
#algoritma

#input
N = int(input("Masukkan Nilai N : "))
petak = [0 for i in range(N)]
jarakPandang = [0 for i in range(N)]

#proses
for i in range(N):
  petak[i] = int(input(f"Tinggi petak ke-{i+1} : "))

for j in range(N):
  valid = True
  for k in range(j-1,-1,-1):
    if petak[k] <= petak[j] and j != 0 and valid:
      jarakPandang[j] += 1
    else:
      valid = False

#output
print("Batas pandang belakang bernilai : " , end="")
for i in range(N):
  if i == N-1:
    print(f'{jarakPandang[i]} ', end="")
  else:
    print(f'{jarakPandang[i]} - ', end="")

