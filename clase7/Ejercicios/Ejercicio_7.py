# 7. Ejercicio Combinado

# Desarrolla un programa que:

# 1. Genere una lista de 10 números aleatorios entre 1 y 20

import random

numeros_aleatorios = [random.randint(1, 20) for x in range(1,11)]
print("La lista de números es: ", numeros_aleatorios,". De los cuales:")

# 2. Usa un bucle for con range para iterar sobre la lista.
# 3. Usar continue para saltar números menores de 10.
# 4. Usar break para detener la iteración si se encuentra un número divisible por 15.

lista_final = []

for x in (numeros_aleatorios):
    if x < 10:
        continue
    elif x % 15 == 0:
        break
    lista_final.append(x)

# 5. Imprimir todos los números que cumplen las condiciones.
for x in lista_final:
    print(f"El número {x} cumple con las condiciones.")
    
# 6. Utilizar list comprehension para filtrar los números que no cumplen ninguna condición.
numeros_filtrados = [x for x in numeros_aleatorios if x >= 10 and x % 15 != 0]