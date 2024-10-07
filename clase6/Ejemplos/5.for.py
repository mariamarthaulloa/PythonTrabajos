# Progrma para imprimir cuadrado de números y calcular la suma

# Lista de números
numeros = [1,2,3,4,5]

# Iniciamos variable
suma_cuadrados = 0

# Iterar sobre cada número en la lista
for numero in numeros:
    # Calcular el cuadrado del número
    cuadrado = numero**2
    # Imprimir el cuadrado
    print(f"El cuadrado de {numero} es {cuadrado}")
    # Agregar el cuadrado a la suma
    suma_cuadrados += cuadrado
    
# Imprimir
print(f"La suma de los cuadrados es: {suma_cuadrados}")