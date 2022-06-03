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

# Calcul matrice de corelatie
r = np.corrcoef(x, rowvar=False)
# print(r)
f.salvare(r, variabile_numerice, variabile_numerice, "r.csv")
# Matricea de covarianta
cov = np.cov(x, rowvar=False, ddof=0)
f.salvare(cov, variabile_numerice, variabile_numerice, "cov.csv")

# Standardizare matrice de observatii
x_std = f.standardizare(x)
x_c = f.standardizare(x, scal=False)
f.salvare(x_std, nume_instante, variabile_numerice, "x_std.csv")
f.salvare(x_c, nume_instante, variabile_numerice, "x_c.csv")

n, m = np.shape(x)
# assert isinstance(x_std,np.ndarray)
# r_ = (1/n)*x_std.T@x_std
# print(r_)
# cov_ = (1 / n) * x_c.T @ x_c
# f.salvare(cov_)

# Teste de concordanta
rez_teste = f.teste_concordanta(x)
f.salvare(rez_teste[0],
          variabile_numerice,
          ["Stat Shapiro", "P Shapiro", "Stat KS", "P KS", "Stat Chi2", "P Chi2"],
          "teste.csv")
nd_variabile = np.array(variabile_numerice)
print("Variabilele care urmeaza distributia normal-gaussiana conform Shapiro Test:")
print(nd_variabile[rez_teste[1][:, 0]])
print("Variabilele care urmeaza distributia normal-gaussiana conform KS Test:")
print(nd_variabile[rez_teste[1][:, 1]])
print("Variabilele care urmeaza distributia normal-gaussiana conform Chi2 Test:")
print(nd_variabile[rez_teste[1][:, 2]])

t_r = f.tabelare(r,variabile_numerice,variabile_numerice)
t_r.to_csv("r_pd.csv")
