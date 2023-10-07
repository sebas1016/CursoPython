# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 14:03:39 2023

@author: sberrio81
"""
import matplotlib.pyplot as plt
espacio_muestral = [(i,j)for i in range(1,7) for j in range (1,7)]
#print(espacio_muestral)
evento_A = [(i,j)for i, j in espacio_muestral if i+j >= 8]
"""
print("+"*50)
print(evento_A)
"""
probabilidad_A=100*(len(evento_A)/len(espacio_muestral))
print(f"probabilidad de obtener valores mayores o iguales a 8 es: {probabilidad_A}%")

evento_B = [(i,j)for i,j in espacio_muestral if i%2 == 0]
#print(evento_B)
probabilidad_B = 100*(len(evento_B)/len(espacio_muestral))
print(f"probabilidad de obtener valores pares con el primer dado es: {probabilidad_B}%")

x_A, y_A = zip(*evento_A)
x_B, y_B = zip(*evento_B)

#print(x_B, y_B)

plt.scatter(x_A, y_A, color='b', label='Evento A : Suma >= 8')
plt.scatter(x_B, y_B, color='r', label='Evento B : Numero par en el primer dado')
plt.xlabel('Resultado dado 1')
plt.ylabel('resultado Dado 2')
plt.title('eventos A y B en el lanzamiento de Dados')
plt.legend()
plt.show()