import pandas as pd
import numpy as np
import functii as f

tabel = pd.read_csv("Mortalitate.csv", index_col=0)
# print(tabel,type(tabel))
nume_instante = list(tabel.index)
nume_variabile = list(tabel.columns)
# print(nume_variabile,nume_instante,sep="\n")
x = tabel.values
# print(x,type(x))

# Inlocuire valori lipsa cu mediile

f.nan_replace(x)

# Calcul matrice de corelatii
r = np.corrcoef(x, rowvar=False)
# print("Matrice de corelatii:", r, sep="\n")

# Salvare matrice corelatii in fisier csv
f.salvare(r, nume_variabile, nume_variabile, "r.csv")
# Calcul matrice de covarianta
cov = np.cov(x, rowvar=False, ddof=0)
f.salvare(cov, nume_variabile, nume_variabile, "cov.csv")

# Standardizare/centrare tabel de observatii
x_std = f.standardizare(x)
x_c = f.standardizare(x, scal=False)
f.salvare(x_std, nume_instante, nume_variabile, "x_std.csv")
f.salvare(x_c, nume_instante, nume_variabile, "x_c.csv")

n, m = x.shape

# Calcul corelatii/covariante din matrice standardizate/centrate
# r_ = (1/n)*x_std.T@x_std
# cov_ = (1/n)*x_c.T@x_c
# print(cov_)

# Aplicare teste de concordanta pentru verificarea distributiei variabilelor
rezumat_teste = f.teste_concordanta(x,p=0.005)
f.salvare(rezumat_teste[0],
          nume_variabile,
          ["Stat Shapiro", "P_value Shapiro", "Stat KS", "P_value KS",
           "Stat Chi2", "P_value Chi2"],
          "t.csv")
print("Variabile care urmeaza disributia normala cf. test Shapiro:")
nd_variabile = np.array(nume_variabile)
print(nd_variabile[rezumat_teste[1][:, 0]])
print("Variabile care urmeaza disributia normala cf. test KS:")
print(nd_variabile[rezumat_teste[1][:, 1]])
print("Variabile care urmeaza disributia normala cf. test Chi2:")
print(nd_variabile[rezumat_teste[1][:, 2]])
