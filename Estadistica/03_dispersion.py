# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:59:44 2023

@author: sberrio81
"""
import numpy as np
import matplotlib.pyplot as plt

horas_estudio = [4,5,6,3,6,7,8,6,5,7,3,7,4,5]
media = np.mean(horas_estudio)
rango = max(horas_estudio)-min(horas_estudio)
varianza = np.var(horas_estudio, ddof=1)
desviacion_estandar = np.std(horas_estudio, ddof=1)
print(f"El rango es: {rango}")
print(f"La varianza es: {varianza}")
print(f"La desviación estandar es: {desviacion_estandar}")
print(f"LA media es: {media}")

plt.scatter(range(1,len(horas_estudio)+1), horas_estudio)
plt.axhline(y=media, color='r', linestyle='--',label='Media')
plt.xlabel('Estudiantes')
plt.ylabel('Horas estudio')
plt.title('Horas de estudio para el examen')
plt.show()