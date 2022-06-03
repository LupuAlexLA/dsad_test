import pandas as pd
import numpy as np
import functii as f

tabel = pd.read_csv("FreeLancer.csv", index_col=1)
# print(tabel,type(tabel),sep="\n")
nume_instante = list(tabel.index)
nume_variabile = list(tabel.columns)
# print(nume_instante, nume_variabile, sep="\n")
variabile_numerice = nume_variabile[2:]
x = tabel[variabile_numerice].values

# Inlocuire valori lipsa
f.nan_replace(x)

# print(x, type(x), sep="\n")
# Calcul matrice de corelatii
r = np.corrcoef(x, rowvar=False)
# print(r)
# f.salvare(r,variabile_numerice,
#           variabile_numerice,"r.csv")
f.salvare(r, nume_coloane=variabile_numerice,
          nume_fisier="r.csv")

# Standardizare matrice
x_std = f.standardizare(x)
f.salvare(x_std, nume_instante,
          variabile_numerice,
          "x_std.csv")

# Verificare repartitie
rez_teste = f.teste_concordanta(x)
f.salvare(rez_teste[0],
          variabile_numerice,
          ["Stat Shapiro", "P Shapiro", "Stat KS", "P KS", "Stat Chi2", "P Chi2"],
          "teste.csv")

nd_variabile = np.array(variabile_numerice)
print("Variabile care urmeaza distributia normal-gaussiana conform Shapiro:")
print(nd_variabile[rez_teste[1][:, 0]])
print("Variabile care urmeaza distributia normal-gaussiana conform KS:")
print(nd_variabile[rez_teste[1][:, 1]])
print("Variabile care urmeaza distributia normal-gaussiana conform Chi2:")
print(nd_variabile[rez_teste[1][:, 2]])
