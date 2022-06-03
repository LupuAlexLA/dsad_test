import pandas as pd
import numpy as np

tabel = pd.read_csv("ADN_Tari.csv", index_col=1)
# print(tabel,type(tabel))
nume_instante = list(tabel.index)
nume_variabile = list(tabel.columns)
print(nume_instante, nume_variabile, sep="\n")
variabile_numerice = nume_variabile[1:]

x = tabel[variabile_numerice].values
# print(x,type(x))

# Calcul matrice de corelatii
r = np.corrcoef(x, rowvar=False)
# print(r)
# Salvare matrice de corelatii

f_out = open("r.csv", "w")
f_out.write("Variabile,")
f_out.write(",".join(nume_variabile))
f_out.write("\n")
n, m = x.shape
for i in range(m):
    f_out.write(variabile_numerice[i] + ",")
    r[i, :].tofile(f_out, sep=",")
    f_out.write("\n")
f_out.close()
