def diversitate(tabel):
    t = []
    for i in tabel:
        instanta_noua = []
        instanta_noua.append(i[0])
        medie = sum(i[2:len(i)]) / (len(i) - 2)
        var = 0
        for j in range(2, len(i)):
            var = var + (i[j] - medie) * (i[j] - medie)
        instanta_noua.append(var / (len(i) - 2))
        t.append(tuple(instanta_noua))
    return t


def filtru_I1(instanta):
    if instanta[2] > 10:
        return True
    else:
        return False


def filtru(instanta, k, l1, l2):
    if instanta[k] >= l1 and instanta[k] <= l2:
        return True
    else:
        return False


def sort(instanta, k):
    return instanta[k]


def selectie(instanta, *k):
    instanta_noua = []
    for i in k:
        instanta_noua.append(instanta[i])
    return tuple(instanta_noua)
