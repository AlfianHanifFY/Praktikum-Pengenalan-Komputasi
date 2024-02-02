#nama/nim : Alfian Hanif Fitria Yustanto / 19623281
#tanggal : 5 Oktober 2023
#Deskripsi : Program game turn based

#kamus
#role_P1 : string
#role_P2 : string
#HP_P1 : float
#HP_P2 : float
#ATK_P1 : intefer
#ATK_P2 : integer
#HP_P1_max : integer
#HP_P2_max : integer
#mulai = boolean
#ronde = integer
#algoritma

#input pemain 1
role_P1 = input("Masukkan role pemain 1 : ")
HP_P1 = 10 #inisiasi awal
HP_P1_max = 0 #inisiasi awal
while(HP_P1 > HP_P1_max):
  if role_P1 == "warrior":
    HP_P1_max = 100
    ATK_P1 = 10
    HP_P1 = float(input("Masukkan sisa HP warrior (P1) : "))
  elif role_P1 == "archer":
    HP_P1_max = 150
    ATK_P1 = 10
    HP_P1 = float(input("Masukkan sisa HP archer (P1) : "))
  elif role_P1 == "paladin":
    HP_P1_max = 100
    ATK_P1 = 5
    HP_P1 = float(input("Masukkan sisa HP paladin (P1) : "))
  if(HP_P1 > HP_P1_max):
    print("HP tidak valid ! ")

#input pemain 2
role_P2 = input("Masukkan role pemain 2 : ")
HP_P2 = 10       #inisiasi awal
HP_P2_max = 0      #inisiasi awal
while(HP_P2 > HP_P2_max):
  if role_P2 == "warrior":
    HP_P2_max = 100
    ATK_P2 = 10
    HP_P2 = float(input("Masukkan sisa HP warrior (P2) : "))
  elif role_P2 == "archer":
    HP_P2_max = 150
    ATK_P2 = 10
    HP_P2 = float(input("Masukkan sisa HP archer (P2) : "))
  elif role_P2 == "paladin":
    HP_P2_max = 100
    ATK_P2 = 5
    HP_P2 = float(input("Masukkan sisa HP paladin (P2) : "))
  if(HP_P2 > HP_P2_max):
    print("HP tidak valid ! ")

#inisiasi awal ronde
mulai = True
ronde = 0

#proses
while(mulai):
  #fase penentuan hasil
  if HP_P1 <= 0 and HP_P2 <= 0:
    print("Permainan berakhir dengan hasil seri.")
    mulai = False
  elif HP_P1 <= 0:
    print("Pemain 2 menang dalam", ronde, "ronde.")
    mulai = False
  elif HP_P2<=0:
    print("Pemain 1 menang dalam", ronde, "ronde.")
    mulai = False
  if(ronde > 100): #jika permainan tidak mungkin selesai
    print("Permainan berakhir dengan hasil seri.")
    mulai = False
  #fase menyerang
  HP_P2 = HP_P2 - ATK_P1 
  HP_P1 = HP_P1 - ATK_P2
  #fase regenerasi
  if role_P1 == "paladin":
    HP_P1 += HP_P1*(10/100)
  if role_P2 == "paladin":
    HP_P2 += HP_P2*(10/100)
  
  ronde += 1  


            

  