#Ejercicio 4: Manipulación de Tuplas y Comprobación de Índices

# Paso 1: Crea una tupla llamada frutas con los siguientes elementos: ("manzana", "banana", "cereza").
mi_tupla = ("manzana", "banana", "cereza")

# Paso 2: Usa el método index para encontrar la posición de la fruta "banana".
banana = (mi_tupla.index("banana"))
print("Banana está en la posición",banana)

# Paso 3: Verifica si la fruta "naranja" está en la tupla. Si no está, muestra un mensaje indicando que no está presente.
naranja = "naranja"

if naranja in mi_tupla:
    print("Naranja sí está presente en la Tupla")
else:
    print("Naranja no está presente en la Tupla.")