# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:12:27 2021

@author: PC
"""

def Fibonacci(n):
   

    if n < 0:
        print("input salah")
 

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

fb = int(input("Masukan sebuah bilangan: "))
print("bilang fibonanci ke",fb," adalah:",Fibonacci(fb))
