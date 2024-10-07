# 1. Ejercicio de Sets y for

# Crea un programa que reciba una lista de números y realice las siguientes operaciones:
lista_numeros = input("Por favor ingresa una lista de 5 números separados por comas: ").split(",")
print(lista_numeros)

# Convertir todos los elementos a int usando map
lista_num = list(map(int, lista_numeros))
print(lista_num)

# 1. Crear un set a partir de la lista para eliminar duplicados.
nueva_lista = set(lista_num)
print(nueva_lista)

# 2. Iterar sobre el set e imprimir cada número.
for numeros in nueva_lista:
    print(numeros)

#3. Contar cuántos números son mayores que un valor dado y almacenarlos en un nuevo set.
valor_dado = 3
suma = 0
numeros_mayores = set() # Conjunto vacío que almacenará los números mayores a 3

for numeros in nueva_lista:
    if numeros > valor_dado:
        suma += 1
        numeros_mayores.add(numeros)
print(f"Dentro de la lista {suma} números son mayores que {valor_dado},")
print(f"Los números mayores que {valor_dado} son: {numeros_mayores}")

    