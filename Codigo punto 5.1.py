import numpy as np

# Matriz A del sistema linealizado
A = np.array([[0, 1], [-2, -0.5]])

# Encontrar los valores y vectores propios
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Valores propios:", eigenvalues)
print("Vectores propios:", eigenvectors)
