def medie(tabel, index_variabila=7):
    s = 0
    for i in tabel:
        s = s + i[index_variabila]
    return s / len(tabel)


def filtru1(instanta):
    if instanta[2] == "EU":
        return True
    else:
        return False


def filtru2(instanta, index_variabila, limita):
    if instanta[index_variabila] > limita:
        return True
    else:
        return False


def sort1(instanta):
    return instanta[5]


def sort2(instanta, index_variabila):
    return instanta[index_variabila]


def mapare(x, index_variabila):
    return x[index_variabila]


def mapare2(x, *indecsi):
    noua_instanta = []
    for i in indecsi:
        noua_instanta.append(x[i])
    return tuple(noua_instanta)
