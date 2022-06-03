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
n, m = x.shape

# Eliminare valori lipsa
f.inlocuire_nan(x)

# Calcul matrice de corelatie
r = np.corrcoef(x, rowvar=False)
# print(r)
f.salvare_matrice(r, nume_variabile, nume_variabile, "r.csv")
v = np.cov(x, rowvar=False, ddof=0)
f.salvare_matrice(v, nume_variabile, nume_variabile, "cov.csv")
# Calcul matrice standardizata
x_std = f.standardizare_centrare(x)
x_c = f.standardizare_centrare(x, False)
f.salvare_matrice(x_std, nume_instante, nume_variabile, "x_std.csv")
f.salvare_matrice(x_c, nume_instante, nume_variabile, "x_c.csv")

n = x.shape[0]
# r_ =  (1/n)*x_std.T@x_std
# v_ = (1/n)*x_c.T@x_c
# print(v_)

# Aplicare teste statistice
# Teste de concordanta
t = f.teste(x)
f.salvare_matrice(t, nume_variabile,
                  ["s_shapiro", "p_shapiro", "s_ks", "p_ks", "s_chi2", "p_chi2"],
                  "teste.csv"
                  )
vector_variabile = np.array(nume_variabile)
decizie_shapiro = t[:, 1] > 0.05
print("Variabile care urmeaza distributia normala cf. Shapiro:", vector_variabile[decizie_shapiro])
decizie_ks = t[:, 3] > 0.05
print("Variabile care urmeaza distributia normala cf. KS:",
      vector_variabile[decizie_ks])
decizie_chi2 = t[:, 5] < 0.05
print("Variabile care urmeaza distributia normala cf. Chi2:",
      vector_variabile[decizie_chi2])
