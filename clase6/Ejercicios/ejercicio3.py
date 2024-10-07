# 3. Ejercicio con range, enumerate, y break/continue

# Escribe un programa que:

# 1. Itere sobre una lista de cadenas usando enumerate para mostrar el índice y el valor.
lista_nombres = ["Aura","Marhta","Emi","Zari","","Berni"]

for indice, nombre in enumerate(lista_nombres):
    # Utilizar continue para saltar cadenas vacías
    if nombre == "":
        continue
    print(f"Indice {indice}: {nombre}")
# Utilizar break si se encuentra una cadena con más de 5 caracteres
    if len(nombre) > 5:
        print(f"Se encontró una cadena con más de 5 caracteres: {nombre}.")
        break