# Paso 1 definimos nombre del archivo
nombre_archivo = "archivo.txt"

# Paso 2: Leemos todo el contenido de una sola vez
with open(nombre_archivo, "r") as archivo:
    print("Leyendo el archivo de una vez con read()")
    contenido_completo = archivo.read()
    print(contenido_completo)
    print("-" * 40)
    
# Paso 3: Leer el archivo línea por línea
with open(nombre_archivo,"r") as archivo: