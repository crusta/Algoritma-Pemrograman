Created on Mon Oct  4 13:40:00 2021

@author: PC
"""
print("Test Segitiga !")
a=int(input("Masukan nilai sisi a: "))
b=int(input("masukan nilai sisi b: "))
c=int(input("masukan nilai sisi c: "))

if a == b == c:
    print("segitiga sama sisi")
elif (a + b <= c) or (a + c <= b) or (b + c <= a) :
    print("bukan segitiga")
elif (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a) :
    print("segitiga siku siku")
elif (a == b) or (a == c) or (b == c) :
    print("segitiga sama kaki")
else :
    print("segitiga sembarang")
