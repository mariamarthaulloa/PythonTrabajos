# Ejercicio 5: Diccionario dentro de una Lista

# 1. Crea una lista de diccionarios donde cada diccionario representa un producto en una tienda, con claves:
lista_de_diccionarios = [{"nombre":"naranja",
                         "precio":5,
                         "Cantidad en stock":15},
                         {"nombre":"pera",
                          "precio":15,
                          "cantidad en stock": 22},
                         {"nombre": "manzana",
                          "precio":12,
                          "cantidad en stock":2}
]

# 2. Imprime el nombre y el precio del segundo producto en la lista.
nombre = lista_de_diccionarios[1]["nombre"]
precio = lista_de_diccionarios[1]["precio"]
print(f"El nombre del producto es ´{nombre}´ y su precio es ´{precio}´")