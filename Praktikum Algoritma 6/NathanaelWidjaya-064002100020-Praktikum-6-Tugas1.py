Created on Mon Nov  1 14:24:01 2021

@author: PC
"""


def rata2(data):
    x = sum(data)/len(data)
    return x

def masuk():
    x = str(input('Masukkin nilai: '))
    return x

def konversi(nilai):
    
        if nilai == 'A' or nilai == 'a': 
            x = float(4.00)
        elif nilai == 'A-' or nilai == 'a-':
            x = float(3.75)
        elif nilai == 'B+' or nilai == 'b+':
            x = float(3.50)
        elif nilai == 'B' or nilai == 'b':
            x = float(3.00)
        elif nilai == 'B-' or nilai == 'b-':
            x = float(2.75)
        elif nilai == 'C+' or nilai == 'c+':
            x = float(2.50)
        elif nilai == 'C' or nilai == 'c':
            x = float(2.00)
        elif nilai == 'C-' or nilai == 'c-':
            x = float(1.75)
        elif nilai == 'D' or nilai == 'd':
            x = float(1.50)
        elif nilai == 'E' or nilai == 'e':
             x = float(1.25)
        else:
            print('Saya tidak mengerti...')
            x = 0
        return x

# Alur

semua = []
data = ''
print('Masukin "selesai, bila ingin nilai rata rata."\n Masukan nilai siswa: ')
while data != 'selesai':
    data = masuk()
    if data == 'selesai':
        break
    skor = konversi(data)
    print(skor)
    semua.append(skor)

print('Nilai rata rata adalah:',rata2(semua))
