# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 20:13:24 2021

@author: PC
"""

# NAMA: NATHANAEL WIDJAYA
# NIM : 064002100020
# TGS : JUMLAH HARI DALAM SUATU BULAN MENGGUNAKAN FUNGSI.

def ganti_tahun(tahun):
    if tahun % 400 == 0:
        return True
    if tahun % 100 == 0:
        return False
    if tahun % 4 == 0:
        return True
    return False

def hari_dalam_bulan(bulan, tahun):
    if bulan in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if bulan == 2:
        if ganti_tahun(tahun):
            return 29
        return 28
    return 30

ulang = "y"
while ulang == "y" or ulang == "yes" or ulang == "ya" or ulang == "iya":
    x = int(input("Masukan bulan:"))
    y = int(input("Masukan tahun:"))
    print("\nbulan tersebut memiliki:",hari_dalam_bulan(x, y),".")
    ulang = input("Mau coba lagi: iya/tidak: ")
    
