import functii as f

nume_fisier = "ADN_Tari.csv"

fisier = open(nume_fisier, "r")
# print(type(fisier))

# Citire din fisier linie cu linie
linii = fisier.readlines()
# print(linii)

nume_variabile = linii[0][:-1].split(",")
# print(nume_variabile)

# Preluare date in lista de tupluri
tabel = []
for i in range(1, len(linii)):
    t = linii[i][:-1].split(",")
    instanta = [t[0], t[1]]
    for j in range(2, len(t)):
        instanta.append(float(t[j]))
    tabel.append(tuple(instanta))
print("Tabelul de date:")
for i in tabel:
    print(i)

# Calcul diversitate genetica
tabel_diversitate = f.diversitate(tabel)
print("Diversitate:")
for i in tabel_diversitate:
    print(i)

# Filtrare

i_filtru = filter(f.filtru_I1, tabel)
tabel1 = [i for i in i_filtru]
print("Tari ca valori mai mari decat 10 pentru I1:")
for i in tabel1:
    print(i)
k = 2
limita1 = 10
limita2 = 20
i_filtru1 = filter(
    lambda x: f.filtru(x, k, limita1, limita2),
    tabel)
tabel2 = [i for i in i_filtru1]
print("Tari cu valori pentru", nume_variabile[k],
      "intre", limita1, "si", limita2, ":")
for i in tabel2:
    print(i)

k = 7
# Sortare dupa o variabila
tabel3 = sorted(tabel,key=lambda x:f.sort(x,k))
print("Tabelul sortat dupa",nume_variabile[k])
for i in tabel3:
    print(i)

# mapare

i_map = map(lambda x:f.selectie(x,0,2,4,6,8),tabel)
tabel4 = [i for i in i_map]
# print(tabel4)

# Salvare in fisier text
f_out = open("out.csv","w")
for i in tabel4:
    linie = [str(j) for j in i]
    f_out.write(",".join(linie))
    f_out.write("\n")
