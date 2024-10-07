# Ejemplo 1 - Callback operación básica

def suma(a,b):
    return a+b
def restar(a,b):
    return a-b

# Función que recibe otra función como Callback
def operar(a,b,funcion_callback):
    resultado = funcion_callback(a,b)
    print(f"Resultado de la operación: {resultado}")

# Uso de la función operar con diferentes callbacks
print(" Ejemplo de Callback simple")
operar(5,3,suma)
operar(5,3,restar)

# Uso de una lambda como Callback
operar(5,3,lambda a,b: a*b)
operar(5,3,lambda a,b:a/b)