# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:44:44 2023

@author: sberrio81
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

media = 10
desviacion_estandar = 2
valor_objetivo = 12
 #calcuo probabilidad con distribución acumulada CDF
probabilidad = norm.cdf(valor_objetivo, media,desviacion_estandar)
print(f"Probabilidad de ser menor o igual a 12: {probabilidad*100}%")
#Calculo funcion de densidad de probabilidad PDF
X = np.linspace(media- 4*desviacion_estandar, media+4*desviacion_estandar,1000)
#print(X)
pdf = norm.pdf(X,media,desviacion_estandar)
#Crreamos la grafica
plt.plot(X,pdf,label='PDF N(10,2)')
plt.fill_between(X, pdf, where=(X<=12),color='blue',alpha=0.3,label='P(x<=12)')
plt.xlabel('Valore')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución normal')
plt.legend()
plt.show()

