A = [[1, 2, 3], [4, 5, 6]]
B = [[-1, 1], [0, 1], [1, 1]]
matrices = (A, B)

# Calcular matrices
C = []
for i in range(len(matrices[0])):
    fila = []
    for j in range(len(matrices[1][0])):
        elemento = 0
        for k in range(len(matrices[1])):
            elemento += matrices[0][i][k] * matrices[1][k][j]
        fila.append(elemento)
    C.append(fila)

# Imprimir el producto de las matrices 
for fila in C:
    print(fila)