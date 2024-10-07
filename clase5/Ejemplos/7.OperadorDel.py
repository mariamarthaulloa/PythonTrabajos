# Crear diccionario
estudiante = {
    "nombre": "Laura",
    "edad": 22,
    "curso": "Ingenieria",
    "ciudad": "Barcelona"
}

# Imprimimos el diccionario
print("Diccionario original: ",estudiante)

# Eliminar el elemento con la clave "curso" usando del
del estudiante["curso"]

# Imprimimos el diccionario después de eliminar el curso
print("Diccionario después de eliminar curso: ", estudiante)
