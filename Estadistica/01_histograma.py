import matplotlib.pyplot as plt

edades = [22,31,25,35,21,19,22,32,19,32,30,31,29,36,32,29,19,21,24,26,27,24,28,26,27,31,31,25,35,21,19,22,32,19,32,31,]
#histograma
plt.hist(edades, bins=10, edgecolor='orange')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.title('Histograma de edades de estudiantes')
plt.show()