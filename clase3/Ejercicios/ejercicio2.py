#Ejercicio 2: Suma de Sublistas

# Paso 1: Define una lista de números predefinida.
mi_lista = [1515,68484,64561,54654,654654,811,51]

# Paso 2: Pide al usuario que ingrese el índice de inicio y el índice de fin para la sublista.
print("De la siguiente lista: ", mi_lista)
indice_inicio = int(input("Por favor ingresa el índice de inicio para la sublista: "))
indice_final = int(input("Por favor ingresa el índice de fin para la sublista: "))

# Paso 3: Usa slicing para obtener la sublista.
sublista = mi_lista[indice_inicio:indice_final]

# Paso 4: Suma los elementos de la sublista.
suma = sum(sublista)

# Paso 5: Muestra la suma.
print("La suma de la sublista es:", suma)