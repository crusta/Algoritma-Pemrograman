"""
Created on Fri Oct  8 21:08:28 2021

@author: PC
"""

"""
Created on Fri Oct  8 20:58:36 2021

@author: PC
"""

print("Nama : Nathanael Widjaya\nNIM  : 064002100020")
print("-----------------------------")
print("program untuk mencari Akar Persamaan Kuadrat dan Determinan")
print("-----------------------------")
import math
 
print("Rumus menggunakan: ax^2 + bx + c = 0")
a = float(input("Masukan, a = "))
b = float(input("Masukan, b = "))
c = float(input("Masukan, c = "))
print("-----------------------------")
det = b * b - 4 * a * c
print("Hasil Determinan: ",det)
if (det<0) :
  print("Tidak Memiliki Akar Persamaan Kuadrat.")
else :
  x1 = (b + math.sqrt(det))/(2 * a)
  x2 = (b - math.sqrt(det))/(2 * a)
  print("Hasil Akar Persamaan Kuadrat =", x1,"atau", x2)
