
import functii
# Acces la functia sum din spatiul builtins
suma = sum([10,20,30,1000])
print(suma)
x = [20,30]
print(functii.sum(x))

def sum(x):
    suma = 0
    for v in x:
        suma+=v
    return suma
