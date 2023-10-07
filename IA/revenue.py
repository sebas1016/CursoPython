# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:52:51 2023

@author: sberrio81
"""

import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Importando Datos
sales_df = pd.read_csv("datos_de_ventas.csv")

#Visualización
sns.scatterplot(x=sales_df['Temperature'],y=sales_df['Revenue'])

#Creando set de entrenamiento
X_train = sales_df['Temperature']
y_train = sales_df['Revenue']

#Creando Modelo
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units = 1, input_shape = [1]))

model.summary()

model.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss = 'mean_squared_error')

#Entrenamiento
epochs_hist = model.fit(X_train, y_train, epochs = 1000)

epochs_hist.history.keys()

#Grafico de entrenamiento del modelo
plt.plot(epochs_hist.history['loss'])
plt.title('Progreso de perdida durante Entrenamiento del modelo')
plt.xlabel('Epoch')
plt.ylabel('Trainig loss')
plt.legend('Training loss')

model.get_weights()

#Predición
Temp = 50
Revenue = model.predict([Temp])
print('La ganancia segun la red neuronal sera: ',Revenue)

#Grafico de prediccion
plt.scatter(X_train,y_train, color='gray')
plt.plot(X_train,model.predict(X_train), color='red')
plt.ylabel('Ganancia [dolares]')
plt.xlabel('Temperatura [gCelsius]')
plt.title('ganancia generada vs Temperatura @Empresa Helados')
