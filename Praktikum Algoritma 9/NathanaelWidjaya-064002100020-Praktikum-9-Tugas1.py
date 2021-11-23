def readwrite():
    biodata = str(f"""Nama : {nama}
umur : {umur}
alamat : {alamat}
Emali : {email}
Dosen Wali : {dosenwali}""")
    write = open("Biodata.txt","r+")
    write.write(biodata)
    write.close()
    read = open("Biodata.txt","r")
    print(f"\n\n{read.read()}")
    
nama = str(input("nama : "))
umur = str(input("umur : "))
alamat = str(input("alamat : "))
email = str(input("email : "))
dosenwali = str(input("dosen wali : "))
readwrite()
