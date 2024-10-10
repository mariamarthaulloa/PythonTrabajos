# Ejercicio 3: Eliminar un archivo TXT

# Escribe un programa que verifique si el archivo archivo_para_eliminar.txt existe. 
# Si existe, elimínalo; si no, muestra un mensaje diciendo que no existe.

import os

nombre_archivo = 'archivo_para_eliminar.txt'

if os.path.exists(nombre_archivo):
    os.remove(nombre_archivo)
    print(f"{nombre_archivo} eliminado.")
else:
    print(f"{nombre_archivo}")