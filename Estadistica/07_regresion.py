# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:56:39 2023

@author: sberrio81
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

ventas = np.array([50,60,70,80,90,70,80,90,65,35])
publicidad = np.array([30,40,50,60,70,40,50,30,25,65])
coef_correlacion = np.corrcoef(ventas,publicidad)[0,1]
print(f"Coeficiente de correlacion de pearson {coef_correlacion}")
#Creamos modelo
model= LinearRegression()
#Ajustar el modelo
model.fit(publicidad.reshape(-1,1), ventas)
#coef pendiente y la interseccion
pendiente = model.coef_[0]
interseccion = model.intercept_
#generamos las predicciones
ventas_pred = model.predict(publicidad.reshape(-1,1))
print(ventas_pred)
#grafica
plt.scatter(publicidad, ventas, label = 'Ventas / Gastos publicidad')
plt.plot(publicidad,ventas_pred,color = 'red',label='Regresion lineal')
plt.xlabel('Gastos publicidad')
plt.ylabel('Ventas')
plt.title("Ventas / Gastos publicidad")
plt.legend()
plt.show()
#mostramos valores
print(f"Pendiente {pendiente}")
print(f"Interseccion: {interseccion}")