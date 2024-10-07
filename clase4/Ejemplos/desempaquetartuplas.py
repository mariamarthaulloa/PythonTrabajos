# Ejemplo 1: desempaquetado de tuplas
# Crear una tupla con varios tipos de datos
mi_tupla = (1, "python", 3.14)

# Desempaquetar la tupla
numero, lenguaje, pi = mi_tupla

# Mostrar el valor de cada variable después del desempaquetado
print("Número: ", numero)
print("Lenguaje: ", lenguaje)
print("Valor de pi: ", pi)

# Ejemplo 2: número de variables no coincide con el número de elementos
# Crear una Tupla con tres elementos
mi_tupla = (1,"python",3.14)

# Intentar desempaquetar en dos variables (causa error)
# numero, lenguaje = mi_tupla

# Ejemplo 3: desempaquetando con el operador *
# Crear una tupla con varios elementos
mi_tupla = (1,"python",3.14,"tuplas","desempaquetado")
# Desempaquetar la tupla con el operador * para capturar varios elementos
primer_elemento, *resto = mi_tupla
# Mostrar los resultados del desempaquetado
print("\nPrimer elemento: ",primer_elemento)
print("Resto de los elementos: ",resto)
