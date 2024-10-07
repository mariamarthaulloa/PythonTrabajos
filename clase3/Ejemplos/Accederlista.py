# Definimos una lista
mi_lista = ["a","b","c","d","e"]

# Acceso usando índices positivos
primer_elemento = mi_lista[0]
print("Primer elemento: ", primer_elemento)

segundo_elemento = mi_lista[1]
print("Segundo elemento: ", segundo_elemento)

# Acceso a índices negativos
ultimo_elemento = mi_lista[-1]
print("Último elemento: ", ultimo_elemento)

penultimo_elemento = mi_lista[-2]
print("Penúltimo elemento: ", penultimo_elemento)

# Acceso a la sublista (slicing)
print("Sublista (índice 1 a 3): ", mi_lista[1:4])
print("Sublista (inicio a 3): ", mi_lista[ :3])
print("Sublista (indice 2 a final): ", mi_lista[2:])

print("//////////////////////////////////")

# Acceso con paso en slicing
print("Sublista con paso 2: ", mi_lista[::2])
print("Sublista con paso 2 en rango (1 a 4): ", mi_lista[1:4:2])

#Iteración a través de una lista
print("Iteración a través de la lista: ")

for elemento in mi_lista:
    print(elemento)