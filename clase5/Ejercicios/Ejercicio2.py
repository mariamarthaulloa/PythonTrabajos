# Ejercicio 2: Modificar y Eliminar Elementos de un Diccionario

# 1. Usando el diccionario del ejercicio anterior, actualiza el año de publicación a 1968.
libro = {
    "Titulo":"La casa de los espiritus",
    "Autora": "Isabel Allende",
    "Año de publicación": 1982,
    "Genero": "Novela"
}

libro["Año de publicación"] = 1968
print("Diccionario con año de publicacion actualizado: ",libro)

# 2. Elimina el género del diccionario.
del libro["Genero"]
print("Diccionario sin la clave de genero: ",libro)

#3. Imprime el diccionario después de cada operación.

