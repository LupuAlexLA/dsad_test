import functii

nume_fisier = "FreeLancerT.csv"

fisier_text = open(nume_fisier, "r")

# print(type(nume_fisier), type(fisier_text))

linii = fisier_text.readlines()
# print(linii)
variabile = linii[0][:-1].split(",")
# print(variabile)

tabel = []
for i in range(1, len(linii)):
    t = linii[i][:-1].split(",")
    instanta = [t[0], t[1], t[2]]
    for j in range(3, len(t)):
        instanta.append(float(t[j]))
    tabel.append(tuple(instanta))
print("Tabelul de date:")
for instanta in tabel:
    print(instanta)

# Calcul medii pe variabile
index_variabila = 7
print("Media pe variabila", variabile[index_variabila],
      "este", functii.medie(tabel, index_variabila=index_variabila))

# Filtrari
# Filtrare tari dupa continent
filtru1 = filter(functii.filtru1, tabel)
tabel1 = [i for i in filtru1]
print("Tari din Europa:")
for i in tabel1:
    print(i)
# Filtrare prin functie lambda
limita = 10
filtru2 = filter(lambda x: functii.filtru2(x, index_variabila, limita),
                 tabel)
tabel2 = [i for i in filtru2]
print("Tari cu procent pentru", variabile[index_variabila],
      "mai mare decat", limita, ":")
for tara in tabel2:
    print(tara)

# Sortari
# Sortare tari dupa o tehnologie
i_sortare1 = sorted(tabel, key=functii.sort1)
tabel3 = [i for i in i_sortare1]
print("Tarile sortate dupa Html", tabel3, sep="\t")

# Sortare tari prin functie lambda
i_sortare2 = sorted(tabel,
                    key=lambda x: functii.sort2(x, index_variabila),
                    reverse=False)
tabel4 = [i for i in i_sortare2]
print("Tarile sortate dupa", variabile[index_variabila], ":")
for tara in tabel4:
    print(tara)

# Mapare

i_map = map(lambda x: functii.mapare(x, index_variabila), tabel)
variabila = [i for i in i_map]
print("Setul de inregistrari pentru variabila",
      variabile[index_variabila], ":")
print(variabila)

i_map1 = map(lambda x: functii.mapare2(x, 0, 5, 7), tabel)
tabel5 = [i for i in i_map1]
print("Tabel nou:")
for i in tabel5:
    print(i)
