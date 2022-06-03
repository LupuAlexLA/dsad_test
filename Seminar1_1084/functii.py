def media(tabel, k):
    s = 0
    for i in tabel:
        s = s + i[k]
    return s / len(tabel)


def filtru_regiune(instanta):
    if instanta[2] == "c":
        return True
    else:
        return False


def filtru(instanta, k, limita1, limita2):
    if instanta[k] >= limita1 and instanta[k] <= limita2:
        return True
    else:
        return False


def sort1(instanta):
    return instanta[2]


def sort2(instanta, k):
    return instanta[k]

def selector(instanta,*k):
    i = []
    for j in k:
        i.append(instanta[j])
    return tuple(i)

