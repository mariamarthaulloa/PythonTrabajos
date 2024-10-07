# Crear un diccionario
persona = {
    "nombre": "Martha",
    "edad": 27,
    "ciudad": "Ensenada",
    "profesion": "Economista"
}

# Eliminar el último clave-valor
clave_valor_eliminado = persona.popitem()
print("El último clave-valor eliminado es: ",clave_valor_eliminado)