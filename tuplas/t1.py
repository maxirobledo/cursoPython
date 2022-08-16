# Ordenación de un diccionario a través de tuplas
from operator import truediv


c = {'a':10, 'b':1, 'c':22}
tmp = list()
for (k,v) in c.items():
    tmp.append((v,k))
tmp = sorted(tmp)
print(tmp)