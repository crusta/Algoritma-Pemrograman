# NAMA : NATHANAEL WIDJAYA
# NIM  : 064002100020
# TUGAS: PRAKTIKUM 4 LAT 2 MENGENAI HARI DALAM SATU BULAN DENGAN INPUT BULAN DAN TAHUN.
# membuat perulangan 
ulang = "y"
while ulang == "y" or ulang == "yes" or ulang == "ya" or ulang == "iya":
    # membuat input yang akan dimasukan kedalam penghitungan 
    bulan = int(input("Masukan bulan: ")) # input bulan dalam int 
    tahun = int(input("Masukan Tahun: ")) # input tahun dalam bulan yang dicari
    # membuat perhitungan hari dalam bulan yang ditentukan
    if (bulan == 1):
        hari = 31
    elif(bulan == 2):
        # mencari apakah tahun kabisat atau tidak dengan perhitungan dibawah
        if((tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0):
            hari = 29 # bila tahun kelipatan empat maka itu kabisat
        else:
            hari = 28 # bila tidak atau false itu merupakan bulan biasa bukan kabisat 
    elif(bulan == 3):
        hari = 31
    elif(bulan == 4):
        hari = 30
    elif(bulan == 5):
        hari = 31
    elif(bulan == 6):
        hari = 30
    elif(bulan == 7):
        hari = 31
    elif(bulan == 8):
        hari = 31
    elif(bulan == 9):
        hari = 30
    elif(bulan == 10):
        hari = 31
    elif(bulan == 11):
        hari = 30
    elif(bulan == 12):
        hari = 31
    else:
        hari = -1
    # OUTPUT
    print("\nbulan tersebut memiliki:",hari,",hari dalam satu bulan.")
    ulang = input("Mau coba lagi: iya/tidak: ")
