#Ejercicio 5: Manejo de Matrículas en una Tupla

# Paso 1: Crea una tupla llamada matriculas con los siguientes números de matrícula: (101, 102, 103, 104, 105).
matriculas_tupla = (101, 102, 103, 104, 105)

# Paso 2: Usa el método count para contar cuántas veces aparece el número de matrícula 102 en la tupla.
numero = matriculas_tupla.count(102)
print("El número 102 aparece",numero, "veces en la Tupla.")

# Paso 3: Usa el método index para encontrar la posición del número de matrícula 104 en la tupla.
posicion = matriculas_tupla.index(104)
print("El número 104 se encuentra en la posición",posicion,"en la Tupla.")