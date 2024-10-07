# Ejercicio 8: Modificar un Valor en un Diccionario Anidado

#1. Crea un diccionario que contenga información sobre una tienda de libros, con las siguientes claves:
#o nombre_tienda
#o libros, que es una lista de diccionarios, donde cada diccionario representa un libro con claves titulo y precio.

tienda_libros = {
    "nombre_tienda":"Libruri",
    "Libros": [{
        "titulo": "Reina de las moscas",
        "precio":445},
        {
        "titulo":"Grandes Dragones",
        "precio":487},
        {
        "titulo":"Bettlejuice",
        "precio":233}]
}
    
#2. Cambia el precio del segundo libro en la lista a un nuevo valor (por ejemplo, 15.99).
Precio = tienda_libros["Libros"][1]
print(Precio)
Precio["precio"] = 155
print(tienda_libros)

#3. Imprime el título y el precio del segundo libro después de la modificación.
print(f"El título y el precio del segundo libro es: ´{Precio}´")