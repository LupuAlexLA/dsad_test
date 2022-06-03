import functii as f

nume_fisier = "Buget2016_judet.csv"

fisier = open(nume_fisier, "r")
# print(type(fisier))
# Citire date din fisier
linii = fisier.readlines()
fisier.close()
# print(linii)
nume_variabile = linii[0][:-1].split(",")
# print(nume_variabile)
tabel = []
for i in range(1, len(linii)):
    t = linii[i][:-1].split(",")
    instanta = [t[0]]
    for j in range(1, len(t)):
        instanta.append(float(t[j]))
    tabel.append(tuple(instanta))
print("Tabelul de date:")
for i in tabel:
    print(i)
# Calcul medii pe variabile
index_variabila = 6
print("Valoarea medie pentru variabila ",
      nume_variabile[index_variabila], "este",
      f.media(tabel=tabel, k=index_variabila))

# Filtrare date
i_filtru1 = filter(f.filtru_TotalVenituri, tabel)
tabel1 = [i for i in i_filtru1]
print("Judete cu TotalVenituri>700000000:")
for i in tabel1:
    print(i)
index_variabila = 1
minim = 700000000
maxim = 800000000
i_filtru2 = filter(lambda x: f.filtru(x, index_variabila, minim, maxim), tabel)
print("Judete cu", nume_variabile[index_variabila],
      "cuprins intre", minim, "si", maxim, ":")
for i in i_filtru2:
    print(i)

# Sortare
index_variabila = 7
tabel2 = sorted(tabel, key=lambda x: f.sortare_dupa_o_variabila(x, index_variabila))
print("Judetele sortate dupa", nume_variabile[index_variabila], ":")
for i in tabel2:
    print(i)

# Transformari
i_map = map(lambda x: f.selectie(x, 0, 1, 2, 3), tabel)
tabel3 = [i for i in i_map]
print("Noul tabel:")
for i in tabel3:
    print(i)

# Salvare in fisier text
out = open("t.csv", "w")
for i in tabel3:
    out.write(",".join([str(j) for j in i]))
    out.write("\n")
out.close()
