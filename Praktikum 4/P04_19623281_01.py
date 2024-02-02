#NIM / Nama : 19623281/Alfian Hanif Fitria Yustanto
#Tanggal    : 2 November 2023
#Deskripsi  : Program mencari nilai diskriminan dan menentukan bentuk akar-akar dari sebuah persamaan kuadrat

#Kamus
# a : integer
# b : integer
# c : integer
# nilaiDiskriminan : prosedur (return float)
# akarKuadrat : prosedur (return string)

#Algoritma  

#Input
a = float(input("Masukkan nilai a : "))
b = float(input("Masukkan nilai b : "))
c = float(input("Masukkan nilai c : "))

#Proses

#subprogram menentukan nilai diskriminan
def nilaiDiskriminan(a,b,c):
  diskriminan = b**2 - (4*a*c)
  return diskriminan

#subprogram menentukan bentuk akar-akar kuadrat
def akarKuadrat(diskriminan):
  if diskriminan > 0:
    return "Persamaan kuadrat memiliki akar berbeda. "
  elif diskriminan == 0:
    return "Persamaan kuadrat memiliki akar kembar. "
  else: #diskriminan < 0
    return "Persamaan kuadrat tidak memiliki akar real. "



#Output
print(f"Nilai diskriminan : {nilaiDiskriminan(a,b,c)}")
print(akarKuadrat(nilaiDiskriminan(a,b,c)))