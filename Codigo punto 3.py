import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import StateSpace, step

# Definir la matriz A
A = np.array([[0, 1], [-2, -0.5]])

# Definir la matriz B
B = np.array([[0], [1]])

# Definir la matriz C
C = np.array([[0, 1]])

# Definir la matriz D
D = np.array([[0]])

# Crear el sistema de espacio de estados
sys = StateSpace(A, B, C, D)

# Simular la respuesta del sistema a una entrada tipo escalón
t, y = step(sys)

# Graficar la respuesta del sistema
plt.plot(t, y)
plt.xlabel('Tiempo (s)')
plt.ylabel('Salida')
plt.title('Respuesta a una entrada tipo escalón')
plt.show()

