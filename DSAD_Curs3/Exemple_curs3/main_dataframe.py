import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

# Instantiere
varsta = [40, 56, 30, 35, 28]
pacienti = pd.DataFrame(
    data={
        "Nume": ['Pop Adrian', 'Popescu Flavius', 'Ionescu Diana', 'Popa Maria', 'Comsa Ioan'],
        "Varsta": varsta,
        "Greutate": [79.5, np.NaN, 78.4, 67, np.NaN],
        "Sectie": ["P", "P", "C", "C", "P"]
    },
    index=range(1, 6)
)

print("Tabel pacienti:")
print(pacienti)

print("\nAdresari prin at/loc, iat/iloc:")
print("pacienti.at[1, \"Nume\"]:",pacienti.at[1, "Nume"],sep="\n")
print("pacienti.iat[0, 0]:",pacienti.iat[0, 0],sep="\n")
print("pacienti.loc[2:4, \"Nume\":]",pacienti.loc[2:4, "Nume":],sep="\n")
print("pacienti.iloc[1:4, 0:]",pacienti.iloc[1:4, 0:],sep="\n")


