import functii as f

nume_fisier = "Teritorial.csv"
# print(nume_fisier,type(nume_fisier))

fisier = open(nume_fisier, "r")
# Citire din fisier linie cu linie
linii = fisier.readlines()
fisier.close()

# print(linii)
nume_variabile = linii[0][:-1].split(",")
# print(nume_variabile)
# Preluare date in lista de tupluri
tabel = []
for i in range(1, len(linii)):
    t = linii[i][:-1].split(",")
    tabel.append((t[0], t[1], t[2], int(t[3]), float(t[4]), float(t[5])))
print("Tabelul de date:")
for i in tabel:
    print(i)
k = 4
print("Media pentru variabila",
      nume_variabile[k],
      "este",
      f.media(tabel, k=k))

# Filtrare de date
i_filtru1 = filter(f.filtru_regiune, tabel)
tabel1 = [i for i in i_filtru1]
print("Judete din regiune Centru:")
for judet in tabel1:
    print(judet)

l1 = 30000
l2 = 40000
i_filtru2 = filter(lambda x: f.filtru(x, k, l1, l2), tabel)
tabel2 = [i for i in i_filtru2]
print("Judete cu", nume_variabile[k], "intre", l1, "si", l2, ":")
for judet in tabel2:
    print(judet)

# Sortari
i_sort1 = sorted(tabel, key=f.sort1)
print("Judetele sortate dupa regiune:")
for i in i_sort1:
    print(i)

i_sort2 = sorted(tabel, key=lambda x: f.sort2(x, k))
print("Judetele sortate dupa", nume_variabile[k], ":")
for i in i_sort2:
    print(i)

# Mapare
i_map1 = map(lambda x: f.sort2(x, k), tabel)
v = [i for i in i_map1]
print("Setul de date pentru variabila", nume_variabile[k], ":")
print(v)

i_map2 = map(lambda x: f.selector(x, 0, 4, 5), tabel)
tabel3 = [i for i in i_map2]
# print(tabel3)

# salvare in fisier text
f_out = open("t.csv", "w")
variabile = [nume_variabile[0], nume_variabile[4], nume_variabile[5]]
f_out.write(",".join(variabile))
f_out.write("\n")
for i in tabel3:
    t = [str(j) for j in i]
    f_out.write(",".join(t))
    f_out.write("\n")
f_out.close()
