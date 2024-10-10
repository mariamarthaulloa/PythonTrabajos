# Ejercicio 8: Usar raise

# Crea un programa que solicite el ingreso de un número entre 1 y 10. Si el
# número no está en ese rango, genera una excepción con raise.

numero_ingresado = int(input("Por favor ingresa un número entre 1 y 10: "))

if numero_ingresado < 1 or numero_ingresado > 10:
    raise ValueError("El número que ingresaste es incorrecto")
else:
    print("¡Muchas gracias!")