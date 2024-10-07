# Programa que pide número hasta que se ingrese el número negativo

# Iniciamos la varibale suma para acumular la suma de los 
# números positivos ingresados.
suma = 0

# Iniciamos un ciclo infinito usando While True
while True:
    # Solicitamos al usuario que introduzca un número
    entrada = int(input("Introduce un número negativo para terminar): "))
                  
    # Verificamos si el número ingresado es negativo
    if entrada < 0:
        #Si el número es negativo salimos del cliclo usando
        break
        
    # Sumamos el número positivo ingresado a la variable suma
    suma += entrada
    
    # Verificar si el número ingresado es par
    if entrada % 2 == 0:
        # Si el número es par usamos continue para saltar la impresión
        # y pasar a la sigueinte iteración del ciclo
        continue
    # Si el número ingresado no es par se ejecuta esta línea:
    print(f"Número impar ingresado: ´{entrada}")
    
# Mensaje final
print(f"El ciclo ha terminado porque se ingresó un número negativo.")
print(f"La suma de los número ingresados es: ´{suma}")
