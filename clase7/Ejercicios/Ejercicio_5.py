# 5. Ejercicio de for con enumerate y break/continue

# Escribe un programa que:
# 1. Itere sobre una lista de nombres de personas.
# 2. Usar enumerate para mostrar el índice y el nombre.
# 3. Saltar los nombres que empiezan con la letra 'A' usando continue.
# 4. Detener la iteración si se encuentra el nombre 'Carlos' usando break.

lista_nombre = ["Ana","Fran","Zari","Carlos"]

for indice, nombre in enumerate(lista_nombre):
    if nombre[0] == "A":
        continue
    elif nombre == "Carlos":
        break
    print(f"{indice}:{nombre}")
    