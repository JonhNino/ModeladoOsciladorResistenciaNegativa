import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definir matrices del sistema
A = np.array([[0, 1], [-2, -0.5]])
B = np.array([[0], [1]])
C = np.array([0, 1])
D = np.array([0])

# Definir función que describe el sistema
def system(state, t):
    x = state.reshape((2, 1))
    dxdt = A @ x + B * 1
    return dxdt.flatten()

# Definir condiciones iniciales y tiempo de integración
x0 = np.array([1, 0])
t = np.linspace(0, 10, 1000)

# Integrar sistema de ecuaciones diferenciales
x = odeint(system, x0, t)

# Graficar solución en el plano x1-x2
plt.plot(x[:, 0], x[:, 1])
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Diagrama de espacio de estados")
plt.grid()
plt.show()
