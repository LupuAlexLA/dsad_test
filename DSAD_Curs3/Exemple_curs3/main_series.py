import numpy as np
import pandas as pd
# Instantiere serie prin vector numpy
v = np.array([1,2,3,4,5])
s = pd.Series(data=v,copy=True)
print(s)
# Instantiere prin dictionar
note_java_1045 = {
    "Popescu Ion":10,
    "Ionescu Dan":7,
    "Ionescu Diana":8
}
java_1045 = pd.Series(data=note_java_1045)
java_1045.name = "Grupa1045"
print(java_1045)
poo_1045 = pd.Series(data={
    "Popescu Ion": 8,
    "Ionescu Dan": 9,
    "Ionescu Diana": 10
})
print(poo_1045.loc['Ionescu Dan'])
print(java_1045.iloc[2])
# Operatori
print("Calcul medii pe cele doua serii:")
s1 = poo_1045.add(java_1045).div(2)
print(s1)
# Concatenare serii
s2 = java_1045.append(poo_1045)
print(s2)
# Inlocuire valori
print("Inlocuire note de 9 cu note de 6:",poo_1045.replace(to_replace=9,value=6))
print(poo_1045)

