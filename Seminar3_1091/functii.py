import numpy as np
from scipy.stats import shapiro, kstest, norm, chi2


def inlocuire_nan(x):
    is_nan = np.isnan(x)
    # print(is_nan)
    k = np.where(is_nan)
    # print(k)
    x[k] = np.nanmean(x[:, k[1]], axis=0)


# Salvare matrice in formatul:
# ,c_1,c_2,...,c_m
# i_1,x_11,x_12,...,x_1m
# ...
# i_n,x_n1,x_n2,...,x_nm
def salvare_matrice(x, nume_linii=None, nume_coloane=None, nume_fisier="out.csv"):
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


# Standardizare sau centrare matrice
def standardizare_centrare(x, scal=True, ddof=0):
    medii_coloane = np.mean(x, axis=0)
    x_ = x - medii_coloane
    if scal:
        abateri_coloane = np.std(x, axis=0, ddof=ddof)
        x_ /= abateri_coloane
    return x_


# Teste de concordanta: Sahpiro, Kolmogorov-Smirnov,Chi2
# Functia intoarce masiv cu statisticile, astfel:
# s_shapiro_1,p_shapiro_1,s_ks_1,p_ks_1,s_chi2_1,p_chi2_1
# s_shapiro_2,p_shapiro_2,s_ks_2,p_ks_2,s_chi2_2,p_chi2_2
# ...
# s_shapiro_m,p_shapiro_m,s_ks_m,p_ks_m,s_chi2_m,p_chi2_m
def teste(x):
    assert isinstance(x, np.ndarray)
    m = x.shape[1]
    t = np.empty((m, 6))
    for i in range(m):
        v = x[:, i]
        t[i, 0:2] = shapiro(v)
        t[i, 2:4] = kstest(v, 'norm')
        t[i, 4:6] = chi2_test(v)
    return t


def chi2_test(v):
    n = len(v)
    f, l = np.histogram(v, bins="sturges")
    m = len(f)
    media = np.mean(v)
    std = np.std(v)
    d = norm.cdf(l[1:], media, std) - norm.cdf(l[:m], media, std)
    fe = n * d
    s = 0
    for i in range(m):
        if fe[i] != 0:
            s += ((f[i] - fe[i]) * (f[i] - fe[i]) / fe[i])
    p_value = chi2.cdf(s, m - 1)
    return s, p_value
