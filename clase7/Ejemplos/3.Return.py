# Ejemplo 1 - básico de Return

def calcular_cuadrado(numero):
    return numero * numero
resultado = calcular_cuadrado(4)

print("Ejemplo básico de return: ")
print(f"El cuadrado de 4 es {resultado}")

# Ejemplo 2 - de múltiples valores
def obtener_datos():
    nombre = "ana"
    edad = 30
    return nombre, edad # Retorna los valores como tupla
# Asignamos los valores a una variable
nombre, edad = obtener_datos()
print("Ejemplo 2 - Retorno de múltiples valores: ")
print(f"Nombre: {nombre}, Edad: {edad}")
print()

# Ejemplo 3 - Return con condicional
def clasificar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Cero"

resultado1 = clasificar_numero(10)
resultado2 = clasificar_numero(-5)
resultado3 = clasificar_numero(0)

print("Ejemplo 3 - Sin return: ")
print(f"El número 10 es {resultado1}")
print(f"El número -5 es {resultado2}")
print(f"El número 0 es {resultado3}")

# Ejemplo 4: sin return
def mostrar_mensaje():
    print("Esta función no retorna valor.")

resultado = mostrar_mensaje()
print("Ejemplo 4: sin return")
print(f"Valor retornado: {resultado}")

