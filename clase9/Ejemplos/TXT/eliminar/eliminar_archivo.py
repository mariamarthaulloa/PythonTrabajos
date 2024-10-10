import os

nombre_archivo = "archivo.txt"

# Comprobar si existe en la ruta. Devuelve TRue si existe y False si no
if os.path.exists(nombre_archivo):
    # Si el archivo existe procederá a eliminarlo
    os.remove(nombre_archivo)
    print(f"Archivo {nombre_archivo} eliminado")
else:
    #si el archivo no existe informar que no se encontró ndad
    print(f"El archivo {nombre_archivo} no existe")