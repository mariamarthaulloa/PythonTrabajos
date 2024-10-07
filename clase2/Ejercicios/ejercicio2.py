#Ejercicio 2: Categoría de Edad con Operadores Lógicos

edad = float(input("Introduce tu edad: "))

if edad>=0 and edad<=12:
    print("Niño")
    
elif edad>=13 and edad<=19:
    print("Adolescente")
    
elif edad>=20 and edad<=64:
    print("Adulto")
    
elif edad == 65 or edad>65:
    print("Adulto mayor")
