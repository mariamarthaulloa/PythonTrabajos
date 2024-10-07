# 4. Ejercicio de while con Condiciones y Contadores

# Desarrolla un programa que:
# 1. Use un bucle while para generar números de la serie de Fibonacci.
# 2. Continúe generando números hasta que el número actual sea mayor o igual a 100.

# Iniciar las variables para la serie de Fibonacci
a = 0
b = 1
serie_fibonacci = []

while a <= 100:
    serie_fibonacci.append(a)
    numero_siguiente = a + b  
    a = b  
    b = numero_siguiente

# 3. Imprima la serie de Fibonacci generada.
print("Serie de Fibonacci generada hasta llegar a 100 o más:")
print(serie_fibonacci)