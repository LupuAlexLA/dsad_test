import numpy as np
from scipy.stats import shapiro, kstest, norm, chi2
from pandas import DataFrame


def inlocuire_nan(x):
    assert isinstance(x, np.ndarray)
    is_nan = np.isnan(x)
    # print(is_nan)
    k = np.where(is_nan)
    # print(k)
    x[k] = np.nanmean(x[:, k[1]], axis=0)


# Salvare matrice ndarray in fisier text
def salvare(x, nume_linii=None, nume_coloane=None, nume_fisier="out.csv"):
    assert isinstance(x, np.ndarray)
    f = open(nume_fisier, "w")
    if nume_coloane is not None:
        if nume_linii is not None:
            f.write(",")
        f.write(",".join(nume_coloane))
        f.write("\n")
    n = x.shape[0]
    for i in range(n):
        if nume_linii is not None:
            f.write(nume_linii[i] + ",")
        x[i, :].tofile(f, sep=",")
        f.write("\n")
    f.close()


# Standardizare/centrare matrice
def standardizare(x, scal=True, nlib=0):
    x_ = x - np.mean(x, axis=0)
    if scal:
        x_ /= np.std(x, axis=0, ddof=nlib)
    return x_


# Verificare distributie normal-gaussiana
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
    t_test[:, 2] = t_stat[:, 5] > p
    return t_stat, t_test


def chi2_test(v):
    f, l = np.histogram(v, bins='sturges')
    m = len(f)
    n = len(v)
    medie = np.mean(v)
    std = np.std(v)
    d = norm.cdf(l[1:], medie, std) - norm.cdf(l[:m], medie, std)
    fe = n * d
    statistica_test = np.sum((f - fe) * (f - fe) / fe)
    p_value = 1 - chi2.cdf(statistica_test, m - 1)
    return statistica_test, p_value


def tabelare(x, nume_linii=None, nume_coloane=None):
    assert isinstance(x, np.ndarray)
    n, m = x.shape
    if nume_linii is None:
        nume_linii = ["r" + str(i) for i in range(1, n + 1)]
    if nume_coloane is None:
        nume_coloane = ["c" + str(i) for i in range(1, m + 1)]
    tabel = DataFrame(data=x, index=nume_linii, columns=nume_coloane)
    return tabel
