import pandas as pd
import numpy as np
import functii as f

tabel = pd.read_csv("ADN_Total.csv", index_col=0)
# print(tabel,type(tabel))
nume_instante = list(tabel.index)
nume_variabile = list(tabel.columns)
# print(nume_instante, nume_variabile, sep="\n")
variabile_numerice = nume_variabile

x = tabel[variabile_numerice].values
# print(x,type(x))

# Calcul matrice de corelatii
r = np.corrcoef(x, rowvar=False)

# Salvare matrice de corelatii
f.salvare(r, variabile_numerice, variabile_numerice, "r.csv")
cov = np.cov(x, rowvar=False, ddof=0)
f.salvare(cov, variabile_numerice, variabile_numerice, "cov.csv")

# Standardizare/Centrare matrice de observatii
x_std = f.standardizare(x)
x_c = f.standardizare(x, False)
f.salvare(x_std, nume_instante, variabile_numerice, "x_std.csv")
f.salvare(x_c, nume_instante, variabile_numerice, "x_c.csv")

n, m = x.shape

# cov_ = (1/n)*x_c.T@x_c
# r_ = (1/n)*x_std.T@x_std
# print(r_)

# Aplicare teste de concordanta pentru verificarea distributiei normal-gaussiene
r_teste = f.teste_concordanta(x)
f.salvare(r_teste[0],
          variabile_numerice,
          ["Stat Shapiro", "P-value Shapiro",
           "Stat KS", "P-value KS",
           "Stat Chi2", "P-value Chi2"],
          "t.csv")

v_variabile = np.array( variabile_numerice )

print("Variabile care urmeaza o distributie normal-gaussiana (Shapiro):")
print(v_variabile[r_teste[1][:,0]])
print("Variabile care urmeaza o distributie normal-gaussiana (KS):")
print(v_variabile[r_teste[1][:,1]])
print("Variabile care urmeaza o distributie normal-gaussiana (Chi2):")
print(v_variabile[r_teste[1][:,2]])
