#Ejercicio 1: Operaciones Básicas con Tuplas

# Paso 1: Crea una tupla llamada mi_tupla con los siguientes elementos: (5,10, 15, 20, 25).
mi_tupla = (5,10, 15, 20, 25)

# Paso 2: Usa el método count para contar cuántas veces aparece el número 10 en la tupla.
numero_diez = mi_tupla.count(10)
print("El número diez aparece",numero_diez,"veces en la tupla.")

# Paso 3: Usa el método index para encontrar la posición del número 20 en la tupla.
posicion = mi_tupla.index(20)
print("El número 20 aparece en la posición",posicion,"de la Tupla.")
