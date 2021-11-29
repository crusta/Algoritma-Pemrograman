def awal_file():
    a = str(input("isi nama file:"))
    b = str(input("isi file :"))
    file = open(a,"w")
    file.write(b)
    file.close()
    
    file = open(a,"r")
    text = file.read()
    print("isi dari file", a ,"adalah",text)
    file.close    
def ubah_file():
    c = str(input("masukan nama file lagi:"))
    d = str(input("masukan yg ingin ditambahkan:"))
    file = open(c,"a")
    file.write(d)
    file.close()
    
    file = open(c,"r")
    text = file.read()
    print("isi dari file", c ,"adalah",text)
    file.close  
def baca_file():   
    e = str(input("masukan nama file lagi:"))
    file = open(e,"r")
    text = file.read()
    print("isi dari file", e ,"adalah",text)
    file.close
    

ulang = "y"
while ulang == "y" or ulang == "yes" or ulang == "ya" or ulang == "iya":
    src = int(input("'1' untuk mulai baru\n'2' untuk ubah isi file\n'3' untuk membaca file.\nMasukan nomor:"))
    if src == 1:
        awal_file()
    elif src == 2:
        ubah_file()
    elif src == 3:
        baca_file()
    else:
        print("nomor invalid")
    
    ulang = input("Mau coba lagi: iya/tidak: ")
