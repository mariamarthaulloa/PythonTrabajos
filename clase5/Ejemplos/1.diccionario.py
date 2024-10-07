# Ejemplo de diccionario
diccionario_vacio = {}
print("Ejemplo de un diccionario vacío: ", diccionario_vacio)

# Ejemplo básico de un diccionario
diccionario = {
    "nombre": "María",
    "edad": 30,
    "casada": False,
    "hijos": ["Ana","Luis"],
    "dirección": {
        "calle": "La gran via",
        "ciudad":"Madrid"
    }
}
print("Ejemplo de diccionario básico: ",diccionario)

# Ejemplo de diccionario con valores de distintos tipos
diccionario_mixto = {
    "nombre": "Alejandra",
    1: [2,3,4],
    (2,3): "tupla como clave",
}
print("Ejemplo de diccionario mixto: ",diccionario_mixto)