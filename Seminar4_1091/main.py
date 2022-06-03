import pandas as pd

import functii as f

tabel_etnii = pd.read_csv("Ethnicity.csv", index_col=0)
f.nan_replace(tabel_etnii)
# print(tabel_etnii)
variabile_etnii = list(tabel_etnii.columns)[1:]

# Calcul populatie pe etnii la nivel de judet
localitati = pd.read_excel("CoduriRomania.xlsx", index_col=0)
t1 = tabel_etnii.merge(right=localitati, left_index=True, right_index=True)
# print(t1)
g1 = t1[variabile_etnii + ["County"]].groupby(by="County").agg(sum)
assert isinstance(g1, pd.DataFrame)
g1.to_csv("EtniiJudete.csv")

# Calcul populatie pe etnii la nivel de regiune
judete = pd.read_excel("CoduriRomania.xlsx", sheet_name=1, index_col=0)
t2 = g1.merge(judete, left_index=True, right_index=True)
g2 = t2[variabile_etnii + ["Regiune"]].groupby(by="Regiune").agg(sum)
assert isinstance(g2, pd.DataFrame)
g2.to_csv("EtniiRegiuni.csv")

# Calcul populatie pe etnii la nivel de macroregiune
regiuni = pd.read_excel("CoduriRomania.xlsx", sheet_name="Regiuni", index_col=0)
t3 = g2.merge(regiuni, left_index=True, right_index=True)
g3 = t3[variabile_etnii + ["MacroRegiune"]].groupby(by="MacroRegiune").agg(sum)
assert isinstance(g3, pd.DataFrame)
g3.to_csv("EtniiMacroregiuni.csv")

# Calcul indici de diversitate la nivel de localitate
# div1 = tabel_etnii.apply(func=f.diversitate,axis=1)
# div1.to_csv("DiversitateLocalitati.csv")
div1 = tabel_etnii.apply(func=f.diversitate__,axis=1,
                         coloana_denumire="Localitate")
div1.to_csv("DiversitateLocalitati.csv")


# Calcul indici de diversitate la nivel de judet
# div2 = g1.apply(func=f.diversitate_,axis=1)
# div2.to_csv("DiversitateJudete.csv")
div2 = g1.apply(func=f.diversitate__,axis=1)
div2.to_csv("DiversitateJudete.csv")

# Calcul indici de diversitate la nivel de regiune
# div3 = g2.apply(func=f.diversitate_,axis=1)
# div3.to_csv("DiversitateRegiuni.csv")
div3 = g2.apply(func=f.diversitate__,axis=1)
div3.to_csv("DiversitateRegiuni.csv")
