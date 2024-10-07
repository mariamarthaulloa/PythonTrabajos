#Ejercicio 1: Calificación con Operador Ternario

import random
calificacion = random.randint(0, 100)  # Genera un entero entre 0 y 100
print("Aprobado") if calificacion >= 60 else print("Reprobado")
