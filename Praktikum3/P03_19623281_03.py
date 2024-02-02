#nama/nim : Alfian Hanif Fitria Yustanto / 19623281
#deskripsi : Program membuat kata rahasia

#kamus
#kata = string
#arrKata = list of string
#valid = Boolean
#lenkata = integer

#algoritma

#input
kata = input("Masukkan kata yang akan dirahasiakan : ")
arrKata = ["" for i in range(len(kata))]
valid = True
lenkata = 0
for i in range(len(kata)):
  arrKata[i] = kata[i]

for i in range(len(kata)):
  j = i - 1
  valid = True
  
  if arrKata[i] == "*":
    while valid and j >= 0:
      if arrKata[j] == "^" or arrKata[j] == "*":
        valid = False
      else:
        print(arrKata[j], end="")
      
      if j == 0 or not valid:
        print(" ",end="")
      j -= 1

  j = i - 1
  lenkata = 0
  if arrKata[i] == "^":
    while arrKata[j] != "*" and arrKata[j] != "^" and j>=0:
      lenkata += 1
      j -= 1
    if lenkata % 2 != 0:
      for q in range(i-lenkata,i,2):
        if q < i-1:
          print(arrKata[q+1],end = "")
          print(arrKata[q],end="")
        else:
          print(arrKata[q],end="")
    else:
      for q in range(i-lenkata,i,2):
        print(arrKata[q + 1],end="")
        print(arrKata[q],end = "")

    print(" " , end="")
    
    



      