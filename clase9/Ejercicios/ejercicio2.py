# Ejercicio 2: Escribir en un archivo TXT

# Crea un programa que escriba un texto en un archivo nuevo_archivo.txt. Si el archivo ya existe, debe sobrescribir su contenido.

with open('nuevo_archivo.txt', 'w') as archivo:
    archivo.write("Mi nombre es Maria Martha.\n")
    archivo.write("Y este es un nuevo archivo.\n")