# Definire functie pentru calculul mortalitatii totale
def mortalitate_totala(tabel):
    t = []
    for instanta in tabel:
        s = sum(instanta[2:len(instanta)])
        t.append((instanta[0], s, s / (len(instanta) - 2)))
    return t


def filtru_BoliInfectioase(instanta):
    if instanta[2] > 40:
        return True
    else:
        return False


def filtru(instanta, k, limita1, limita2):
    if instanta[k] >= limita1 and instanta[k] <= limita2:
        return True
    else:
        return False


def sortare(instanta, k):
    return instanta[k]
