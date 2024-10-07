# Ejercicio 4: Lista de Diccionarios

# 1. Crea una lista de diccionarios, donde cada diccionario representa un estudiante con las siguientes claves:
lista_de_diccionarios = [{"nombre":"Martha",
                          "edad": 27,
                          "calificaciones":[9,8,7]},
                         {"nombre":"Armando",
                          "edad":31,
                          "calificaciones":[10,10,9]},
                         {"nombre":"Zarina",
                          "edad":30,
                          "calificaciones":[7,8,9]}
]

#2. Imprime el nombre y las calificaciones del primer estudiante en la lista.
nombre = lista_de_diccionarios[0]["nombre"]
calificaciones = lista_de_diccionarios[0]["calificaciones"]
print(f"El nombre del estudiante es ´{nombre}´ y sus calificaciones son: ´{calificaciones}´")