# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:10:10 2023

@author: sberrio81
"""
import numpy as np
from scipy import stats
alturas = [165,170,160,180,190,165,170,170,150,175,185,191,185,172,175,170,191,170,180,190,165,162]

#media

media = np.mean(alturas)

print(f"Media de alturas: {media}")
#otra forma de calcular la media
print("*"*50)
suma = 0
for numero in alturas:
    suma= suma+numero
print(f"La suma de lista es igual a: {suma}")
print(f"La lista tiene {len(alturas)} valores")
media = suma / len(alturas)
print(f"La media es: {media}")
print("*"*50)
#mediana

mediana = np.median(alturas)
print(f"El valor central o mediana es: {mediana}")
print("*"*50)

#Moda
moda = stats.mode(alturas)
print(f"El valor mas frecuente o moda es: {moda.mode[0]}")
print(f"Este ultimo valor se repite: {moda.count[0]} veces")
print("*"*50)




