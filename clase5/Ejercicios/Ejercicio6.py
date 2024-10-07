# Ejercicio 6: Anidación Compleja de Diccionarios y Listas

# 1. Crea un diccionario que contenga información sobre una escuela. La escuela tiene:
escuela = {"nombre":"cide",
           "año de fundacion":1975,
           "Lista de clases": [{"nombre de la clase": "Matematicas",
               "Lista de estudiantes": [{
                   "nombre":"Juan",
                   "edad":20},
                    {"nombre":"Pedro",
                     "edad":21},
                    {"nombre":"Armando",
                     "edad":52}]},
                    {"nombre de la clase":"español",
                     "Lista de estudiantes":[{
                         "nombre":"Martha",
                         "edad":22},
                         {"nombre":"Zarina",
                         "edad":15},
                         {"nombre":"Juan",
                          "edad":20}]}             
           ]
           }

# 2. Imprime el nombre del primer estudiante de la primera clase
lista_clases = escuela["Lista de clases"]

primer_clase = lista_clases[0]["Lista de estudiantes"]

nombre = primer_clase[0]["nombre"]
print(f"El nombre del primer estudiante de la primera clase es ´{nombre}´")