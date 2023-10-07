# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:57:33 2023

@author: sberrio81
"""

import numpy as np

from scipy import stats

import matplotlib.pyplot as plt



# Datos de la muestra

altura_muestra = np.array([168, 172, 165, 175, 170, 169, 171, 168, 173, 174])



# Media de la muestra

media_muestra = np.mean(altura_muestra)



# Media hipotética

media_hipotetica = 170



# Desviación estándar de la muestra

desviacion_estandar = np.std(altura_muestra, ddof=1)



# T estadístico

t_estadistico = (media_muestra - media_hipotetica) / (desviacion_estandar / np.sqrt(len(altura_muestra)))



# Valor crítico t

valor_critico_t = stats.t.ppf(0.975, df=len(altura_muestra)-1)



# Gráfico

x = np.linspace(160, 180, 1000)

y = stats.t.pdf(x, df=len(altura_muestra)-1)

plt.plot(x, y, label='Distribución t')

plt.axvline(x=media_muestra, color='r', linestyle='--', label='Media de la muestra')

plt.axvline(x=media_hipotetica, color='g', linestyle='--', label='Media hipotética')

plt.axvline(x=valor_critico_t * (desviacion_estandar / np.sqrt(len(altura_muestra))) + media_hipotetica, color='b', linestyle='--', label='Valor crítico t')

plt.legend()

plt.xlabel('Altura (cm)')

plt.ylabel('Densidad de Probabilidad')

plt.title('Prueba t de una muestra')

plt.show()



# Resultado

print(f'T estadístico: {t_estadistico}')

print(f'Valor crítico t: {valor_critico_t}')