"""
Created on Mon Oct 18 13:42:51 2021

@author: PC
"""

skor = 0    
nsiswa = list() # ini nanti yang mau di rata2in

ulang = 0
nomor = 0
while ulang == 0:
    nomor += 1
    x = str(input('"selesai" untuk menghitung rata rata!\nNilai siswa: ')) #masukkan huruf
    if x == 'selesai': #kalo keluar keluar
        ulang = 1
    else: # Ubah ke nilai float
        if x == 'A' or x == 'a': 
            skor = float(4.00)
        elif x == 'A-' or x == 'a-':
            skor = float(3.75)
        elif x == 'B+' or x == 'b+':
            skor = float(3.50)
        elif 'B' or x == 'b':
            skor = float(3.00)
        elif x == 'B-' or x == 'b-':
            skor = float(2.75)
        elif x == 'C+' or x == 'c+':
            skor = float(2.50)
        elif x == 'C' or x == 'c':
            skor = float(2.00)
        elif x == 'C-' or x == 'c-':
            skor = float(1.75)
        elif x == 'D' or x == 'd':
            skor = float(1.50)
        elif x == 'E' or x == 'e':
            skor = float(1.25)
        else:
            print('Saya tidak mengerti...')
            skor = 0
        print(('\nNilai ke-{0} = {1}').format(nomor,skor))
        nsiswa.append(skor)
    



rata2 = sum(nsiswa) / len(nsiswa) # total / jumlah = rata2
print('Rata ratanya n:', rata2)
