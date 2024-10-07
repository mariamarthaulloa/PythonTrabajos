#Ejercicio 3: Anidación Básica de Diccionarios

#1. Crea un diccionario que represente una persona con las siguientes claves:
persona = {
    "nombre": "Martha",
    "edad":27,
    "direccion": {
        "calle": "Sicilia",
        "ciudad": "Ensenada",
        "CP": 22890
    }
}

# 2. Imprime la ciudad de la dirección
print("La ciudad es: ",persona["direccion"]["ciudad"])

