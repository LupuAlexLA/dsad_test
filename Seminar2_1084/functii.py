import numpy as np

def inlocuire_nan(x):
    assert isinstance(x,np.ndarray)
    is_nan = np.isnan(x)
    # print(is_nan)
    k = np.where(is_nan)
    # print(k)
    x[k] = np.nanmean( x[:,k[1]],axis = 0 )

