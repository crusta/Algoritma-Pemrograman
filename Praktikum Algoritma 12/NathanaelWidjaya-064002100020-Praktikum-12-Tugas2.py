import pandas as pd

data = {"Negara": ["Indonesia", "Jepang", "India", "China", "Amerika Serikat", "Brazil", "Rusia","Afganistan","Afrika Selatan","Afrika Tengah"],
        "Ibu Kota": ["Jakarta", "Tokyo", "New Delhi", "Beijing", "Washington DC", "Brazilia", "Moskow","Kabul","Pretoria","Bangui"],
        "Benua": ["Asia", "Asia", "Asia", "Asia", "Amerika", "Amerika", "Asia","Asia","Afrika","Afrika"],
        "Luas": [1905, 377, 3287, 9597, 9834, 8515, 17098, 6520, 122000, 62298],
        "Populasi": [264, 143, 1252, 1357, 329, 210, 146, 3893, 5931, 483] }



df = pd.DataFrame(data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

filename = "NegaraStandarDeviasi.csv"
std.to_csv(filename)
filename1 = "NegaraMean.csv"
mean.to_csv("NegaraMean.csv")

print(df)

df1 = pd.read_csv(filename)
print("\n",df1)
print()
df2 = pd.read_csv(filename1)
print(df2)
