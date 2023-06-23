import numpy as np
import matplotlib.pyplot as plt

# Definir las constantes del sistema
L = 1
C = 1
R = -0.5
u = 1
e = np.sqrt(L/C)

# Definir las funciones de la dinámica no lineal del sistema
def f(x, u):
    x1, x2 = x
    dx1 = x2
    dx2 = -x1 - e*(-1 + x1**2)*x2 + u
    return np.array([dx1, dx2])

# Definir el tiempo de simulación
t_sim = 50
dt = 0.01
t = np.arange(0, t_sim, dt)

# Generar la señal aleatoria de la perturbación
mu, sigma = 0, 0.1
noise = np.random.normal(mu, sigma, len(t))

# Definir las condiciones iniciales
x0 = np.array([0, 1])

# Simular la dinámica no lineal del sistema con perturbación aleatoria
x = np.zeros((len(t), 2))
x[0] = x0
for i in range(1, len(t)):
    dx = f(x[i-1], u) * dt
    x[i] = x[i-1] + dx + noise[i]*dt

# Calcular la energía de las señales x1(t) y x2(t) y la energía total
E_x1 = 0.5 * L * x[:,1]**2
E_x2 = 0.5 * C * x[:,0]**2
E_total = E_x1 + E_x2

# Graficar la energía de las señales x1(t) y x2(t), la energía total y la perturbación aleatoria
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(t, E_x1, label='Energía de x1')
ax.plot(t, E_x2, label='Energía de x2')
ax.plot(t, E_total, label='Energía Total')
ax.plot(t, noise, label='Perturbación Aleatoria')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Energía')
ax.set_title('Energía de las señales y perturbación aleatoria')
ax.legend()

# Graficar las barras de la energía de las señales x1(t) y x2(t)
fig, ax = plt.subplots(figsize=(8,6))
ax.bar(['x1', 'x2'], [E_x1[-1], E_x2[-1]])
ax.set_xlabel('Señales')
ax.set_ylabel('Energía')
ax.set_title('Energía de las señales x1(t) y x2(t) al final del tiempo de simulación')
plt.show()




