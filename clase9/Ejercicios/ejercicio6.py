# Ejercicio 6: Manejo básico de errores con try/except

# Crea un programa que solicite al usuario que ingrese un número. Si el
# usuario ingresa algo que no es un número, muestra un mensaje de error usando try/except.


try:
    # Solicitamos al usuario que ingrese un número
    numero = int(input("Por favor, ingresa un número: "))
except ValueError:
    print("Error: Lo que ingresaste no es un número válido.")


