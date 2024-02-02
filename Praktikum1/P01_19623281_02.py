#Nama/NIM : Alfian Hanif Fitria Yustanto/19623281
#Tanggal : 21 September 2023
#Deskripsi : Program menentukan pilihan transportasi paling ekonomis dan biayanya berdasarkan jam keberangkatan dan kepulangan

#kamus
#berangkat = integer
#pulang = integer
#t_berangkat = string
#t_pulang = string

#algoritma

#input
berangkat = int(input("Jam keberangkatan Nona Deb: "))
pulang = int(input("Jam kepulangan Nona Deb: "))

#proses
biaya = 0                                     #biaya awal
if(6<=berangkat<= 8 or 15<=berangkat<=17):
  t_berangkat = "Bus Universitas"
  biaya += 0
elif(8<berangkat<15 or 17<pulang<18):
  t_berangkat = "Bus Kota"
  biaya += 5000
else: #17<berangkat<=24 dan 24<berangkat<6
  t_berangkat = "Travel"
  biaya += 10000

if(6<=pulang<= 8 or 15<=pulang<=17):
  t_pulang = "Bus Universitas"
  biaya += 0
elif(8<pulang<15 or 17<pulang<=18):
  t_pulang = "Bus Kota"
  biaya += 5000
else: #17<berangkat<=24 dan 24<berangkat<6
  t_pulang = "Travel"
  biaya += 10000

print("Nona Deb berangkat naik",t_berangkat,"dan pulang naik",t_pulang,"dengan total biaya",str(biaya),".")
