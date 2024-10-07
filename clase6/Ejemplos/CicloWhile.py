# Programa para adivinar un número secreto

# Definimos el número secreto
numero_secreto = 7

# Iniciar la vriable para almacenar el número del usuario
numero_adivinado = None

# Mensaje inicial
print("Adivina el número secreto (entre 1 y 10): ")

# Bucle while que continua hasta que el usuario adivine el número secreto
while numero_adivinado != numero_secreto:
    # Solicitar al usuario que ingrese un número
    numero_adivinado = int(input("Introduce tu número: "))
    
    # Comprobar si el número adivinado es correcto
    if numero_adivinado < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif numero_adivinado > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print("Adivinaste el número.")
        
# Mensaje de finalización del juego
print("Gracias por jugar.")