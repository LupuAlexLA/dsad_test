def media(tabel, k):
    s = 0
    for instanta in tabel:
        s = s + instanta[k]
    return s / len(tabel)


def filtru_TotalVenituri(instanta):
    if instanta[1] > 700000000:
        return True
    else:
        return False


def filtru(instanta, k, valoare_minima, valoare_maxima):
    if instanta[k] >= valoare_minima and instanta[k] <= valoare_maxima:
        return True
    else:
        return False


def sortare_dupa_o_variabila(instanta, k):
    return instanta[k]


def selectie(instanta, *k):
    noua_instanta = []
    for i in k:
        noua_instanta.append(instanta[i])
    return tuple(noua_instanta)
