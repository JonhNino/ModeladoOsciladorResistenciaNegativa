import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def equations(x, t, L, C, R, e, u):
    x1, x2 = x
    dx1_dt = x2
    dx2_dt = -x1 - e*(-1 + x1**2)*x2 + u
    return [dx1_dt, dx2_dt]

L = 1
C = 1
R = -0.5
u = 1
e = np.sqrt(L/C)

# Define 100 initial conditions
num_conditions = 100
x0_list = np.random.uniform(low=-1, high=1, size=(num_conditions, 2))

# Solve the system for each initial condition
num_points = 1000
t = np.linspace(0, 100, num_points)
sol_list = []

for i in range(num_conditions):
    sol = odeint(equations, x0_list[i], t, args=(L, C, R, e, u))
    sol_list.append(sol)

fig, ax = plt.subplots(figsize=(8, 6))

for i in range(num_conditions):
    ax.plot(t, sol_list[i][:,0], 'b', alpha=0.1)
    
ax.set_xlabel('Tiempo')
ax.set_ylabel('Voltaje')
ax.set_title('Soluciones del sistema no lineal con diferentes condiciones iniciales')
plt.show()
