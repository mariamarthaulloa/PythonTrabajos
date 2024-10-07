# Definir listas

# Lista vacía
lista_vacia = []
print("Lista vacía: ", lista_vacia)

# Lista de elementos iniciales / números
lista_elementos = [1,2,3,4,5]
print("Lista de elementos iniciales: ", lista_elementos)

# Lista de cadenas
lista_cadenas = ["manzana", "banana", "cereza"]
print("Lista de cadenas: ", lista_cadenas)

# Lista Mixta
lista_mixta = [42, "texto", 3.14, [1,2, 3]]
print("Lista mixta: ",lista_mixta)

# Lista con elementos repetidos
lista_repetidos = [0] * 5
print("Lista con elementos repetidos: ",lista_repetidos)

#Lista a partir de otros iterables
cadena = "hola"
lista_de_caracteres = list(cadena)
print("Lista a partir de otros iterables (cadena): ",lista_de_caracteres)