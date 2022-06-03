import numpy as np
from scipy.stats import shapiro, kstest, norm, chi2


def inlocuire_nan(x):
    is_nan = np.isnan(x)
    # print(is_nan)
    k = np.where(is_nan)
    # print(k)
    x[k] = np.nanmean(x[:, k[1]], axis=0)


# Salvare matrice ndarray in fisier text
def salvare_ndarray(x, nume_linii=None, nume_coloane=None, nume_fisier="out.csv"):
    f = open(nume_fisier, "w")
    if nume_coloane is not None:
        if nume_linii is not None:
            f.write(",")
        f.write(",".join(nume_coloane) + "\n")
    n = np.shape(x)[0]
    for i in range(n):
        if nume_linii is not None:
            f.write(nume_linii[i] + ",")
        f.write(",".join([str(v) for v in x[i, :]]) + "\n")
    f.close()


# Standardizare/Centrare matrice
def standardizare(x, scal=True, ddof=0):
    medii = np.mean(x, axis=0)
    x_ = x - medii
    if scal:
        abateri_sdtandard = np.std(x, axis=0, ddof=ddof)
        x_ /= abateri_sdtandard
    return x_


def teste_concordanta(x, p=0.05):
    assert isinstance(x, np.ndarray)
    n, m = x.shape
    t_stat = np.empty((m, 6))
    t_test = np.empty((m, 3), dtype=bool)
    for i in range(m):
        v = x[:, i]
        t_stat[i, 0:2] = shapiro(v)
        t_stat[i, 2:4] = kstest(v, 'norm')
        t_stat[i, 4:6] = chi2_test(v)
    t_test[:, 0] = t_stat[:, 1] > p
    t_test[:, 1] = t_stat[:, 3] > p
    t_test[:, 2] = t_stat[:, 5] < p
    return t_stat,t_test


def chi2_test(v):
    n = len(v)
    f, l = np.histogram(v, bins='sturges')
    m = len(f)
    media = np.mean(v)
    std = np.std(v)
    d = norm.cdf(l[1:], media, std) - norm.cdf(l[:m], media, std)
    fe = n * d
    stat_test = np.sum((f - fe) ** 2 / (fe*fe))
    p_value = chi2.cdf(stat_test, m - 1)
    return stat_test, p_value
