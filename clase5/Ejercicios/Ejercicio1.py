# Ejercicio 1: Crear y Acceder a un Diccionario Básico

# 1. Crea un diccionario que contenga la siguiente información sobre un libro:
libro = {
    "Titulo":"La casa de los espiritus",
    "Autora": "Isabel Allende",
    "Año de publicación": 1982,
    "Genero": "Novela"
}

# 2. Accede e imprime cada uno de estos valores usando las claves correspondientes.

titulo = libro["Titulo"]
print("El titulo del libro es: ",titulo)

autora = libro.get("Autora")
print("La autora del libro es: ",autora)

año = libro["Año de publicación"]
print("El año de publicación del libro es: ",año)

genero = libro.get("Genero")
print("El genero del libro es: ",genero)