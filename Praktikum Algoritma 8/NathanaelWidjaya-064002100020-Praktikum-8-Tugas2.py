def hitung_pangkat(bilangan, pangkat):
  if pangkat > 1:
      return bilangan * hitung_pangkat(bilangan, pangkat - 1)

  return bilangan



hasil = hitung_pangkat(int(input("Masukan bilangan awal: ")),int(input("Masukan pangkat: ")))
print(f'Hasil = {hasil}')
