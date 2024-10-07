# Definir una matriz de 3 por 3
matriz = [
    [1,2,3], # Fila 0
    [4,5,6], # Fila 1
    [7,8,9]  # Fila 2
]

# Acceder y mostrar algunos elementos específicos de la matriz
print("Algunos elmentos de la matriz: ")
print("Elementos en la fila 0, columna 0: ", matriz[0][0])
print("Elemento en la fila 1, columna 2: ", matriz[1][2])

# Modificar elementos específicos de la matriz
print("\nModificando elementos específicos: ")
matriz[0][1] = 10 # Cambiar el elemento en la fila 0, columna 1 a 10.
matriz[2][0] = 15
print("Matriz después de las modificaciones: ")
print(matriz)

# Acceder a una fila completa
print("\nAccediendo a una fila completa: ")
fila_completa = matriz[1] # Obtener toda la fila
print("Fila completa en la posición 1: ", fila_completa)

# Reemplazar una fila completa
print("\nReemplazando una fila completa: ")
matriz[1] = [20,21,22]
print("Matriz después de reemplazar la fila 1: ")
print(matriz)

# Trabajar con una submatriz (parte de una matriz)
submatriz = [matriz[0][1:3], matriz[1][1:3]]
print("Submatriz extraída: ", submatriz)

#Mostramos toda la matriz al final
print("\nMostramos toda la matriz al final: ")
print(matriz[0])
print(matriz[1])
print(matriz[2])