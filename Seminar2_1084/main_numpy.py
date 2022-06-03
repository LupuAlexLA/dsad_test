import pandas as pd
import numpy as np
import functii as f

tabel = pd.read_csv("Teritorial.csv", index_col=0)
# print(tabel,type(tabel),sep="\n")
nume_instante = list(tabel.index)
nume_variabile = list(tabel.columns)
# print(nume_instante,nume_variabile,sep="\n")
variabile_numerice = nume_variabile[3:]

x = tabel[variabile_numerice].values
# print(x, type(x), sep="\n")

f.inlocuire_nan(x)

#Calcul matrice de corelatie
r = np.corrcoef(x,rowvar=False)
print(r)


