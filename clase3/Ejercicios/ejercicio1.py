#Ejercicio 1: Contador de Números Específicos

# Paso 1: Define una lista de números predefinida
mi_lista = [0,1,1,2,3,4,5,5,5,6,6,7,7,7,8,8,9,10,10]

# Paso 2: Pide al usuario que ingrese un número a buscar
numero = int(input("Por favor ingresa un número del 0 al 10 para buscar en la lista: "))

# Paso 3: Usa el método count() para determinar cuántas veces aparece el número en la lista
conteo = mi_lista.count(numero)

# Paso 4: Muestra el resultado
print(f"El número aparece en la lista {conteo} veces")