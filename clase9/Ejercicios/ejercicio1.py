# Ejercicio 1: Leer un archivo TXT

# Crea un programa en Python que lea el contenido de un archivo y muestre cada línea en la consola. El archivo tiene varias
# líneas de texto. Usa el método que prefieras para leer el archivo.

with open('mi_archivo.txt', 'r') as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    print(linea.strip())  