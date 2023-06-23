import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
C = 1
L = 1
R = 0.5
u = 1
e = np.sqrt(L/C)

# Definir la ecuación diferencial
def f(t, x):
    x1, x2 = x
    dx1 = x2
    dx2 = -x1 - e*(-1 + x1**2)*x2
    return [dx1, dx2]

# Crear un arreglo de puntos en el espacio de estados
x1 = np.linspace(-2, 2, 20)
x2 = np.linspace(-2, 2, 20)
X1, X2 = np.meshgrid(x1, x2)

# Calcular el campo vectorial en cada punto del espacio de estados
DX1, DX2 = f(0, [X1, X2])

# Graficar los retratos de fase
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_title('Retratos de fase del sistema')
ax.quiver(X1, X2, DX1, DX2)
plt.show()
