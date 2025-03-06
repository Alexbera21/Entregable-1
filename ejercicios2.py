import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con seno y coseno
df = pd.DataFrame({
    'x': np.linspace(0, 2 * np.pi, 1000),
    'seno': np.sin(np.linspace(0, 2 * np.pi, 1000)),
    'coseno': np.cos(np.linspace(0, 2 * np.pi, 1000))
})

# Graficar
plt.plot(df['x'], df['seno'], label='Seno', color='Yellow')
plt.plot(df['x'], df['coseno'], label='Coseno', color='blue', linewidth=4)  # Doble grosor
plt.title('Funciones Seno y Coseno')
plt.xlabel('x')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()
