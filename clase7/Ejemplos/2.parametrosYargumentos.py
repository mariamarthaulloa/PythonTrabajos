# Definición de una función: parámetros posicionales, con nombre y predeterminados

def presentar_persona(nombre,edad,ciudad="Desconocida",profesion = "Desconocida"):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"ciudad: {ciudad}")
    print(f"Profesión: {profesion}")
    print()
    
# Ejemplos de llamados a la función

# Usando argumentos posicionales
print("Ejemplo con argumentos posicionales: ")
presentar_persona("ana",30)

# Usando argumentos posicionales y con nombre
print("Ejemplo con argumentos posicionales y con nombre: ")
presentar_persona("Luis",25,ciudad="Madrid",profesion="Ingeniero")

# Usando todos los argumentos con nombre
print("Ejemplo de todos los argumentos con nombre: ")
presentar_persona(nombre="Martha",edad=37,ciudad="Madrid",profesion="Ingeniero")
