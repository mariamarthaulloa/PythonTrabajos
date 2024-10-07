# Scope: alcance local y global en python

# Variable global
x = 20

def funcion_local():
    x = 10 # en este caso x es una variable local
    print(f"El valor de x dentro de la función local: {x}")
funcion_local()

def funcion_global():
    global x # Para modificar la variable global
    x = 30
    print(f"Valor de x dentro de la función global: {x}")
funcion_global()
print(f"Valor de x fuera de la función: {x}")
