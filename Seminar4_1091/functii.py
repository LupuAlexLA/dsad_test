import pandas as pd
from pandas.api.types import is_numeric_dtype
import numpy as np


def nan_replace(t):
    assert isinstance(t, pd.DataFrame)
    nume_variabile = list(t.columns)
    for v in nume_variabile:
        if any(t[v].isna()):
            if is_numeric_dtype(t[v]):
                t[v].fillna(t[v].mean(), inplace=True)
            else:
                modulul = t[v].mode()[0]
                t[v].fillna(modulul, inplace=True)


def diversitate__(t, coloana_denumire=None):
    assert isinstance(t, pd.Series)
    if coloana_denumire is not None:
        x = np.array(t.iloc[1:], dtype=float)
    else:
        x = t.values
    s = np.sum(x)
    p = x / s
    k = p == 0
    p[k] = 1
    e = -np.sum(p * np.log2(p))
    p_ = x / s
    s_p = np.sum(p_ * p_)
    simpson = 1 - s_p
    inv_simpson = 1 / s_p
    if coloana_denumire is not None:
        serie_div = pd.Series(
            data=[t.iloc[0], e, simpson, inv_simpson],
            index=[coloana_denumire, "Shannon", "Simpson", "Inverse Simpson"]
        )
    else:
        serie_div = pd.Series(
            data=[e, simpson, inv_simpson],
            index=["Shannon", "Simpson", "Inverse Simpson"]
        )
    return serie_div


def diversitate(t):
    assert isinstance(t, pd.Series)
    x = np.array(t.iloc[1:], dtype=float)
    s = np.sum(x)
    p = x / s
    k = p == 0
    p[k] = 1
    e = -np.sum(p * np.log2(p))
    p_ = x / s
    s_p = np.sum(p_ * p_)
    simpson = 1 - s_p
    inv_simpson = 1 / s_p
    serie_div = pd.Series(
        data=[t.iloc[0], e, simpson, inv_simpson],
        index=["Localitate", "Shannon", "Simpson", "Inverse Simpson"]
    )
    return serie_div


def diversitate_(t):
    assert isinstance(t, pd.Series)
    x = t.values
    s = np.sum(x)
    p = x / s
    k = p == 0
    p[k] = 1
    e = -np.sum(p * np.log2(p))
    p_ = x / s
    s_p = np.sum(p_ * p_)
    simpson = 1 - s_p
    inv_simpson = 1 / s_p
    serie_div = pd.Series(
        data=[e, simpson, inv_simpson],
        index=["Shannon", "Simpson", "Inverse Simpson"]
    )
    return serie_div
