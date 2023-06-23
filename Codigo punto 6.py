import numpy as np

A = np.array([[0, 1], [-2, -0.5]])
B = np.array([[0], [1]])
C = np.array([0, 1])
D = np.array([0])

# Paso 1: Obtener valores y vectores propios
eigenvals, eigenvects = np.linalg.eig(A)

# Paso 2: Crear matriz de cambio de base
P = eigenvects

# Paso 3: Crear matriz diagonal
D = np.diag(eigenvals)

# Paso 4: Calcular matriz inversa de P
P_inv = np.linalg.inv(P)

# Paso 5: Calcular forma diagonal del sistema
A_diag = np.matmul(P_inv, np.matmul(A, P))
B_diag = np.matmul(P_inv, B)
C_diag = np.matmul(C, P)

print("Forma diagonal del sistema:")
print("A =")
print(A_diag)
print("B =")
print(B_diag)
print("C =")
print(C_diag)
print("D =")
print(D)

