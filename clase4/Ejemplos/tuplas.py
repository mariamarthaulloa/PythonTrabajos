# Crear una tupla con varios

tupla_mixta = (1,"Hola",3.5)

# Mostrar completa la tupla
print("Tupla completa: ", tupla_mixta)

# Acceder a los elementos de la tupla por su índice
print("Primer elemento de la tupla: ", tupla_mixta[0])
print("Primer elemento de la tupla: ", tupla_mixta[1])
print("Primer elemento de la tupla: ", tupla_mixta[2])

# Explicación tuplas inmutables
print("\nLas tuplas no se pueden modificar. Intentemos cambiar el primer elemento de la tupla: ")

# Ejemplo de intento que causaría error 
# tupla_mixta[0] = 10

# Explicación clara de la inmutabilidad
print("Si intentamos hacer tupla_mixta[0] = 10, Python mostrará por qué no se puede cambiar ningún elemento de la Tupla")

# Mostramos como sí podemos "modifical" una tupla, creando una
nueva_tupla = (10, "Hola", 3.5)
print("Nueva tupla con el primer elemento cambiado: ", nueva_tupla)
print("Tupla original permanece sin cambios: ", tupla_mixta)


