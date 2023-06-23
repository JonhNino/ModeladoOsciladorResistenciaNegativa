import numpy as np
import matplotlib.pyplot as plt

A = np.array([[0, 1], [-2, -0.5]])
B = np.array([0, 1])
C = np.array([0, 1])
autovalores, autovectores = np.linalg.eig(A)

# Definir la solución fundamental
def solucion_fundamental(t, c1, c2):
    x_fund = np.zeros((2, len(t)), dtype=np.complex128)
    for i in range(len(autovalores)):
        x_fund += np.outer(autovectores[:, i], c1*np.exp(autovalores[i]*t) + c2*np.exp(autovalores[i].conjugate()*t)).astype(np.complex128)
    return x_fund

# Graficar la solución fundamental
t = np.linspace(0, 10, 100)
x0 = np.array([1, 0])
c1 = 1
c2 = 0
x_fund = solucion_fundamental(t, c1, c2)
x = np.real(x_fund[0])
y = np.real(x_fund[1])
plt.plot(t, x, label="x")
plt.plot(t, y, label="y")
plt.xlabel("tiempo")
plt.legend()
plt.show()
