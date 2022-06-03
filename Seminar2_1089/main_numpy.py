import pandas as pd
import numpy as np
import functii as f

tabel = pd.read_csv("mortalitate.csv", index_col=0)
# print(tabel,type(tabel))
nume_instante = list(tabel.index)
nume_variabile = list(tabel.columns)
print(nume_variabile, nume_instante, sep="\n")
variabile_numerice = nume_variabile[1:]

x = tabel[variabile_numerice].values
# print(x,type(x))

# Inlocuire valori lipsa cu mediile

f.inlocuire_nan(x)

# Calcul matrice de corelatii
n, m = x.shape
r = np.corrcoef(x, rowvar=False)
print(r)
