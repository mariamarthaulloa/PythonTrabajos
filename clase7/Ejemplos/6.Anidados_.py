# Ejemplo 1 - básico funciones anidadas

def funcion_externa(x):
    def funcion_interna(y):
        return y + 10
    return funcion_interna(x) # Lamada a la función interna con el valor x

# Llamada a la función externa
resultado = funcion_externa(5)
print(f"Resultado de la función_externa(5): {resultado}")

# Ejemplo 2 - Clousure

def crear_multiplicador(factor): 
    def multiplicador(x):
        return x * factor
    return multiplicador
duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)

print(f"Duplicar 10: {duplicar(10)}")
print(f"Triplicar 10: {triplicar(10)}")