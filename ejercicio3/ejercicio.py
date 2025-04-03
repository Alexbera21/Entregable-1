import numpy as np
import matplotlib.pyplot as plt

# Lista de edades
edades = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

# Calcular media, mediana, varianza y desviación estándar
media, mediana = np.mean(edades), np.median(edades)
varianza = np.var(edades)
desviacion = np.std(edades)

# Graficar el "pano" con líneas
plt.figure(figsize=(6, 4))
plt.plot(edades, marker='o', color='b', linestyle='-', linewidth=2, markersize=6, label='Edades')

# Añadir líneas para la media y la mediana
plt.axhline(media, color='r', linestyle='--', label=f'Media: {media:.2f}')
plt.axhline(mediana, color='g', linestyle='--', label=f'Mediana: {mediana:.2f}')

# Mostrar la varianza y desviación estándar
plt.text(0, media + 2, f'Varianza: {varianza:.2f}\nDesviación Estándar: {desviacion:.2f}', fontsize=10, color='black')

# Añadir título y etiquetas
plt.title("Distribución de Edades", fontsize=12)
plt.xlabel("Índice", fontsize=10)
plt.ylabel("Edades", fontsize=10)

# Mostrar leyenda
plt.legend(loc='upper left', fontsize=10)

# Mostrar la gráfica
plt.show()
