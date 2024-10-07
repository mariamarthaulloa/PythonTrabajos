# Decorador básico

def mi_decorador(func):
    def wrapper(*args,**kwargs):
        print("Antes de ejecutar la función")
        resultado = func(*args,**kwargs)
        print("Después de ejecutar la función")
        return resultado
    return wrapper

# Usamos el decorador en una función
@mi_decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")
    
# Llamados a la función decorada
print("Decorador en una función")
saludar("Ana")

# Decorador con parámetro
def repetir_veces(veces):
    def decorador(func):
        def wrapper(*args,**kwargs):
            for _ in range(veces):
                func(*args,**kwargs)
            return wrapper
        return decorador

@repetir_veces(3)
def decir_hola():
    print("Hola")

print("\nDecorador con parámetro")
decir_hola()
