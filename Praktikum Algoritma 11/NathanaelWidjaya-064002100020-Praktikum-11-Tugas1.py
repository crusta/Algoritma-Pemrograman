class mahasiswa:
    
    jumlah = 0
    
    def __init__(self,nama,nim,tahun):
        self.nama = str(nama)
        self.nim = int(nim)
        self.tahun = str(tahun)
        mahasiswa.jumlah += 1
        
    def biodata(self):
        return str(f'{self.nama};{self.nim};{self.tahun}')
    
    def Display_bio(self):
        print('\nNama:',self.nama)
        print('Nim:',self.nim)
        print('Tahun:',self.tahun)
    
    
        
while True:
    print(f'\nMahasiswa ke -  {(mahasiswa.jumlah)+1}\nKetik "selesai" untuk mengakhiri!')
    a = str(input('Nama: '))
    if a == 'selesai':
        break
    b = int(input('NIM: '))
    c = int(input('Tahun: '))
    
    n = mahasiswa(a,b,c)
    
    n.Display_bio()
