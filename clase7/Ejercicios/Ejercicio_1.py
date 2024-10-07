# 1. Ejercicio de List Comprehension con range y for.

# Crea un programa que:

# 1. Genere una lista de números del 1 al 10 usando range.
lista_numeros = []

for numero in range(1,11,1):
    lista_numeros.append(numero)
    
print(lista_numeros)

# 2. Cree una nueva lista que contenga el cuadrado de cada número solo si el número es impar.
nueva_lista = []
cuadrado_par = []

cuadrado_ipar = [numero**2 for numero in lista_numeros if numero %2 != 0]
print(cuadrado_ipar)