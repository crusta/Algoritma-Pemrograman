#umur <=2 = gratis
#umur 3 - 12 =  $14
#umur >= 65 = $18
#else = $23

skor = 0    
nsiswa = list() # list daftar umur/harga yang dimasukan

ulang = 0
nomor = 0
print("NATHANAEL WIDJAYA - 064002100020")
print()
print("SELAMAT DATANG DI WAHANA SERBA ADA ! ")
while ulang == 0:
    nomor += 1
    x = int(input('"PRESS 0 UNTUK MENGHITUNG TOTAL!"\nMasukan Umur Pembeli: ')) 
    if x == 0: #selesai: perintah untuk menghitung hasil akhir.
        ulang = 1
    else:
        if x <= 2:
            skor = 0
        elif x >= 3 and x <= 12:
            skor = 14
        elif x >= 13 and x <= 64:
            skor = 23
        else:
            skor = 18
        print(("\n harga pembeli ke -{0} = {1}$").format(nomor, skor))
        nsiswa.append(skor)   
       
print("TOTAL BIAYA ADALAH SEBESAR: $",sum(nsiswa))
diterima = int(input("Masukan uang anda: "))      
total = (sum(nsiswa))
kembalian = (diterima - total)
if diterima < total:
    print("Uang anda tidak cukup untuk melakukan pembayaran")
elif diterima == total:
    print("Uang anda pas dan kembalian anda adalah: $",kembalian)
else:
    print("Kembalian anda adalah:$",kembalian)
