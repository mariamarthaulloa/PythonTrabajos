# 2. Ejercicio Integrador

# Desarrolla un programa que haga lo siguiente:

# 1. Usar un bucle for con range para iterar sobre los números del 1 al 20.
# 2. Usar continue para saltar los números divisibles por 3.
# 3. Usar break para detener la iteración si se encuentra un número mayor que 15.
# 4. Crear un set con los números restantes y verificar si algún número es par.

numeros = set() 

for numero in range(1, 21):
    if numero % 3 == 0:
        continue
    elif numero > 15:
        break
    numeros.add(numero)

print(numeros)

# Verificar si algún número es mpar

for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} es un número par")
    