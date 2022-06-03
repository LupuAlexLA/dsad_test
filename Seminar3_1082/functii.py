import numpy as np
from scipy.stats import shapiro, kstest, norm, chi2


# Salvare matrice ndarray in fisier csv
def salvare(x, nume_linii=None, nume_coloane=None, nume_fisier="out.csv"):
    f_out = open(nume_fisier, "w")
    if nume_coloane is not None:
        if nume_linii is not None:
            f_out.write(",")
        f_out.write(",".join(nume_coloane))
        f_out.write("\n")
    n, m = x.shape
    for i in range(n):
        if nume_linii is not None:
            f_out.write(nume_linii[i] + ",")
        x[i, :].tofile(f_out, sep=",")
        f_out.write("\n")
    f_out.close()


def standardizare(x, scal=True, nlib=0):
    x_ = x - np.mean(x, axis=0)
    if scal:
        x_ /= np.std(x, axis=0, ddof=nlib)
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
    return t_stat, t_test


def chi2_test(v):
    n = len(v)
    f, l = np.histogram(v, 'sturges')
    m = len(f)
    media = np.mean(v)
    std = np.std(v)
    d = norm.cdf(l[1:], media, std) - norm.cdf(l[:m], media, std)
    fe = n * d
    stts = np.sum((f - fe) ** 2 / fe)
    p_value = chi2.cdf(stts, m - 1)
    return stts, p_value
