import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

# Instantiere
varsta = [40, 56, 30, 35, 28]
pacienti = pd.DataFrame(
    data={
        "Nume": ['Pop Adrian', 'Popescu Flavius', 'Ionescu Diana', 'Popa Maria', 'Comsa Ioan'],
        "Varsta": varsta,
        "Greutate": [79.5, np.NaN, 78.4, 67, np.NaN],
        "Sectie": ["P", "P", "C", "C", "P"]
    },
    index=range(1, 6)
)

print("Tabel pacienti:")
print(pacienti)

# Reindexare
print("\n-- Reindexare")
print("Tabel:", pacienti, sep="\n")
print("Reindexare:")
print(pacienti.reindex(index=[1.7, 7], method='bfill'))
print(pacienti.reindex(index=[1.7, 7], method='ffill'))
print(pacienti.reindex(index=[1.7, 7], method='nearest'))

print("\n--Selectie pe baza de conditii aplicate coloanelor")
print("Pacienti cu varsta mai mare decat 30:")
print(pacienti[pacienti["Varsta"] > 30])

print("\n--Adaugare:")
print("Tabel pacienti:")
print(pacienti)
print("Adaugare prin serie:",
      pacienti.append(pd.Series(['Pop Eugen', 36], index=['Nume', 'Varsta'], name=13)), sep="\n")
print("Adaugare prin dictionar", pacienti.append(
    {"Nume": "Ion Ion", "Greutate": 105}, ignore_index=True
))

print("Adaugare coloana:")
pacienti['SaturatieO'] = [98, 99, 97, 97, 95]
print(pacienti)

print("\n--Concatenare:")
print("Tabel pacienti:")
print(pacienti)
tabel_concatenare1 = pd.DataFrame(
    data={
        "Temperatura": [39, 37, 36.8, 40, 37.2],
        "Tensiune_d": [8, 6, 6.7, 9, 7]
    }
    # , index=range(1, 6)
)
print("Tabel care se concateneaza pe linii:")
print(tabel_concatenare1)
print("Tabel concatenat:")
pacienti1 = pd.concat([pacienti, tabel_concatenare1], axis=1)
print(pacienti1)
print("Tabel care se concateneaza pe coloane:")
tabel_concatenare2 = pd.DataFrame(data={"Nume": ["Georgescu Liviu", "Popa Mihai"],
                                        "Greutate": (100, 94), "SaturatieO": (80, 92)})
print(tabel_concatenare2)
print("Tabel concatenat:")
pacienti2 = pd.concat([pacienti, tabel_concatenare2], ignore_index=True)
print(pacienti2)

print("\n--Replace")
print("Tabel:", pacienti, sep="\n")
pacienti.replace(to_replace={97: 94}, inplace=True)
print("Inlocuire saturatie 97 cu 94:")
print(pacienti)

print("\n--Modificari")
print("Tabel:", pacienti, sep="\n")
pacienti.update(pd.Series([75, 70], index=[2, 4], name="Greutate"))
print(pacienti)


print("\n--Stergere coloane 'Nume','Greutate':")
print(pacienti.drop(["Nume", "Greutate"], axis=1))

print("\n--Stergere linii cu valori nan:")
print(pacienti.dropna())


print("\n--Inlocuire valori lipsa pentru Greutate cu 80:")
print(pacienti.fillna(value={"Greutate": 80}))
print("\n--Inlocuire valori lipsa cu media:")
print(pacienti.fillna(pacienti.mean()))

print("\n--Sortare inversa dupa numele coloanelor:")
print(pacienti.sort_index(axis=1, ascending=False))
print("\n--Sortare inversa dupa 'Varsta':")
print(pacienti.sort_values(by="Varsta", ascending=False))

print("\n--Identificare pacienti supraponderali (>80 kg) prin apply:")
print("Tabel:", pacienti2, sep="\n")
print(pacienti2.apply(lambda x: "Supraponderal" if x["Greutate"] > 80 else "Normal", axis=1))

print("\n--Agregare la nivel de sectie cu calcul medii pentru coloanele numerice:")
grup = pacienti.groupby(by="Sectie")
print(grup.agg(func=np.mean))

# Instantiere tabel cu indecsi multiplii
studenti = pd.DataFrame(data={
    ("Informatii", "Nume"): ["Popescu Delia", "Ionescu Dan", "Mircea Elena", "Comsa Marius"],
    ("Informatii", "Grupa"): [1075, 1075, 1080, 1081],
    ("Note", "Java"): [8, 9, 7, 6],
    ("Note", "POO"): [7, 7, 6, 8]
}, index=[['A', 'A', 'B', 'B'], np.arange(1, 5)])
index_linii = studenti.index
assert isinstance(index_linii, pd.MultiIndex)
index_linii.set_names(['Seria', 'Id'], inplace=True)
print("\n--Tabel multi-index:", studenti, sep="\n")

# Selectii
print("\n--Selectii")
print("\nSelectie dupa index coloana. Cheie 'Informatii'", studenti['Informatii'], sep="\n")
print("\nSelectie dupa index coloana. Cheie 'Informatii-'Nume'", studenti["Informatii"]['Nume'], sep="\n")
print("\nSelectie dupa index coloana. Cheie 'Informatii-'Nume' si index linie cheie 'A'",
      studenti["Informatii"]['Nume'][('A', 2)], sep="\n")
print("\nSelectie dupa index linie 'A' si coloana 'Note'", studenti.loc['A', "Note"], sep="\n")
print("\nSelectie dupa index linie 'A' si coloana 'Informatii'", studenti.loc['A', "Informatii"], sep="\n")
print("\nSelectie dupa index linie 'A' si coloana ('Informatii','Note')", studenti.loc['A', ("Informatii", "Nume")],
      sep="\n")
print("\nSelectie prin loc", studenti.loc[('A', 1), "Informatii"], sep="\n")
print("\nSelectie prin iloc", studenti.iloc[1:, :3], sep="\n")


# Pivotare prin unstack
print("\n--Exemple unstack")
print("Tabel pivotat:", studenti, sep="\n")
print("Unstack:")
print("level=1", studenti.unstack(level=1), sep="\n")
print("level=0", studenti.unstack(level=0), sep="\n")


# Comutare intre niveluri
print("\nExemple swaplevel")
print("Tabel:", studenti, sep="\n")
print(studenti.swaplevel(axis=0))
print(studenti.swaplevel(axis=1))

# Sortare dupa index
print("\nSortare dupa index:")
print(studenti.sort_index(level=0, ascending=False))

# Eliminare nivel
print("\nEliminare nivel 0 cu rezultat in tabelul 'stud':")
stud = studenti.droplevel(axis=1, level=0).droplevel(level=0)
print(stud, stud.index, stud.columns, sep="\n")

print("\n--Creare tabela 'catalog':")
catalog = pd.DataFrame(
    data={"Probabilitati": [9, 7, 5], 'Nume': ["Comsa Marius", "Popescu Mihai", "Radu Ioana"]},
    index=[3, 4, 5])
catalog.index.name = 'Id'
print(catalog, catalog.index, catalog.columns, sep="\n")

# Jonctiune prin join
assert isinstance(stud, pd.DataFrame)
tabela = stud.join(other=catalog, lsuffix="_1", how="inner")
print("\nJonctiune prin join cu 'inner', 'stud' cu 'catalog' in 'tabela':", tabela, sep="\n")

# Jonctiune prin merge
tabela1 = stud.merge(right=catalog)
print("\nJonctiune prin merge dupa coloana comuna 'Nume' intre 'stud' si 'catalog' in 'tabela1':", tabela1, sep="\n")

# Pivotare
print("\n--Pivotare")
print("Tabel:", stud, "\n")
pivot = stud.pivot(columns="Grupa")
print("\nPivotare 'stud' dupa 'Grupa'", pivot, pivot.index, pivot.columns, sep="\n")

# Liniarizare
print("\n--Liniarizare")
print("Tabel:", studenti, sep="\n")
print("\nLiniarizare 'student' dupa nivelul 1 in indexul de coloana:", studenti.melt(col_level=1), sep="\n")
print("\nLiniarizare coloane 'POO','Java' dupa 'Grupa' si 'Nume'",
      stud.melt(id_vars=['Grupa', 'Nume'], value_vars=['POO', 'Java']), sep="\n")

grupe = pd.Categorical(values=[1045, 1046, 1045, 1050, 1045, 1045, 1046, 1000, 1000], ordered=True)
print("\nVariabila categoriala 'grupe':", grupe, type(grupe), sep="\n")
print("\nCoduri asociate categoriilor variabilei 'grupe':", grupe.codes, type(grupe.codes), sep="\n")
print("\nAdaugare categorie 1070:\n", grupe.add_categories(new_categories=[1070]))
print("\nEliminare categorie 1000:\n", grupe.remove_categories(removals=[1000]))
print("\nEliminare categorii neutilizate:\n", grupe.remove_unused_categories())
