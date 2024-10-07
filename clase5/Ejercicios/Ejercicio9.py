# Ejercicio 9: Buscar y Imprimir la Edad de un Estudiante en un Diccionario Anidado

# 1. Crea un diccionario que represente una clase con los siguientes datos:
#o nombre_clase
#o estudiantes, que es una lista de diccionarios con información de cada estudiante (nombre y edad).
clase = {
    "nombre_clase" : "Matemáticas",
    "estudiantes": [
        {"nombre":"Mateo",
         "edad": 17},
        {"nombre":"Axel",
         "edad": 15},
        {"nombre":"Ramon",
         "edad":14}
    ]
}

#2. Escribe una función que busque la edad de un estudiante dado su nombre usando el índice de la lista en lugar de bucles (suponiendo
#que conoces el índice).
# Función para buscar la edad de un estudiante dado su índice
def edad_por_indice(clase, indice):
    return clase["estudiantes"][indice]["edad"]

# Asignar el índice del estudiante (por ejemplo, el índice 1 es "Axel")
indice_estudiante = 1

# Obtener la edad del estudiante en el índice 1
edad_estudiante = edad_por_indice(clase, indice_estudiante)

#3. Imprime la edad del estudiante buscado.
print(f"La edad del estudiante es: {edad_estudiante}")
