# 2. Ejercicio de while y for

# Definimos el número cero
numero_cero = 0

# Iniciar la lista para almacenar el número que ingresa el usuario
numeros_ingresados = []

# Iniciar variable de número ingresado
numero_ingresado = None

# Mensaje inicial
print("Ingresa números del 1 al 10 [Ingresa 0 para finalizar]: ")

# Bucle while que continua hasta que el usuario ingrece el número 0
while numero_ingresado != numero_cero:
    # Solicitar al usuario que ingrese un número
    numero_ingresado = int(input("Introduce tu número: "))
    
    # Comprobar si el número adivinado es cero
    if numero_ingresado == numero_cero:
        print("Fin del juego.")
    else:
        numeros_ingresados.append(numero_ingresado)
        print("Sigue ingresando números.")
        
# Mensaje de finalización del juego
print("Gracias por jugar.")

# Usar un bucle for para calcular la suma de los números ingresados, excluyendo el 0
suma_numeros = 0
for numero in numeros_ingresados:
    suma_numeros += numero

# Mostrar el resultado de la suma
print(f"La suma de los números ingresados es: {suma_numeros}")