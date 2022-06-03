import pandas as pd
import numpy as np
import functii as f

tabel = pd.read_csv("mortalitate.csv", index_col=0)
# print(tabel,type(tabel))
nume_instante = list(tabel.index)
nume_variabile = list(tabel.columns)
# print(nume_variabile, nume_instante, sep="\n")
variabile_numerice = nume_variabile[1:]

x = tabel[variabile_numerice].values
# print(x,type(x))

# Inlocuire valori lipsa cu mediile
f.inlocuire_nan(x)

# Calcul matrice de corelatii
n, m = x.shape
r = np.corrcoef(x, rowvar=False)
# print(r)
f.salvare_ndarray(r, variabile_numerice, variabile_numerice, "r.csv")
# Calcul matrice de covarianta
v = np.cov(x, rowvar=False, ddof=0)
f.salvare_ndarray(v, variabile_numerice, variabile_numerice, "cov.csv")

# Centrare si standardizare matrice de observatii
x_std = f.standardizare(x)
x_c = f.standardizare(x, scal=False)
f.salvare_ndarray(x_std, nume_instante,
                  variabile_numerice, "x_std.csv")
f.salvare_ndarray(x_c, nume_instante,
                  variabile_numerice, "x_c.csv")
n = x.shape[0]
r_ = (1 / n) * x_std.T @ x_std
# print(r_)
v_ = (1 / n) * x_c.T @ x_c
# print(v_)

# Teste statistice
# Teste de concordanta pentru verificarea legii de repartitie a variabilelor
rezumat_teste = f.teste_concordanta(x)
f.salvare_ndarray(rezumat_teste[0],
                  variabile_numerice,
                  ["S Shapiro", "P Shapiro", "S KS", "P KS",
                   "S Chi2", "P Chi2"],
                  "t.csv")

ndarray_variabile = np.array(variabile_numerice)
print("Variabile care urmeaza legea normala conform Sapiro,Ks,Chi2:")
print(ndarray_variabile[rezumat_teste[1][:, 0]])
print(ndarray_variabile[rezumat_teste[1][:, 1]])
print(ndarray_variabile[rezumat_teste[1][:, 2]])
