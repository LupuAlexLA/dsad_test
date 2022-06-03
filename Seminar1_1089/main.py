import functii as f

nume_fisier = "mortalitate.csv"

# print(type(nume_fisier))

fisier = open(nume_fisier, "r")
# print(type(fisier))

# Citire din fisier
linii = fisier.readlines()
fisier.close()
# print(linii)
nume_variabile = linii[0][:-1].split(",")
# print(nume_variabile)
tabel = []
for i in range(1, len(linii)):
    t = linii[i][:-1].split(",")
    instanta = [t[0], t[1]]
    for j in range(2, len(t)):
        instanta.append(float(t[j]) if t[j] != '' else 0)
    tabel.append(tuple(instanta))
print("Tabelul de date:")
for i in tabel:
    print(i)
tabel_mortalitate = f.mortalitate_totala(tabel)
print("Mortalitatea totala pe judete:")
for i in tabel_mortalitate:
    print(i)

# Salvare tabel_mortalitate in fisier text
f_out = open("out.csv", "w")
f_out.write("Judet,Valoare Totala,Valoare Medie\n")
for i in tabel_mortalitate:
    f_out.write(",".join([str(j) for j in i]))
    f_out.write("\n")
f_out.close()

# Filtrare
# Selectie judete cu mortalitate pentru BoliInfectioase>40
i_filtru = filter(f.filtru_BoliInfectioase, tabel)
tabel1 = [i for i in i_filtru]
print("Judete cu mortalitate pentru BoliInfectioase>40:")
for i in tabel1:
    print(i)

k = 5
l1 = 20
l2 = 30
i_filtru1 = filter(lambda x: f.filtru(x, k, l1, l2), tabel)
print("Judete cu mortalitate pentru",
      nume_variabile[k], "cuprinsa intre", l1, "si", l2, ":")
for i in i_filtru1:
    print(i)

# Sortare dupa o variabila
k=2
tabel2 = sorted(tabel, key=lambda x: f.sortare(x, k))
print("Judetele sortate dupa mortalitate la",
      nume_variabile[k], ":")
for i in tabel2:
    print(i)
