# 6. Ejercicio de List Comprehension y range

# Crea un programa que:
# 1. Use range para generar una lista de números del 1 al 15.
# 2. Utilice list comprehension para crear una nueva lista con el cubo  de los números pares.

nueva_lista = [i**3 for i in range (1,16) if i % 2 == 0 ]
print(nueva_lista)