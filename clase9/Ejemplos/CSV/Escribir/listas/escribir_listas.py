import csv

fieldnames = ["Nombre","Edad","Ciudad"]

# New line se utiliza para evitar lineas en blanco adicionales
with open("archivo.csv", "w", newline="") as file:
    # Creamos un objeto Dicwritter
    # se pasa el archivo y la lista de nombresde columnas
    writter = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Escribir la fila de encabezados en el archivo csv
    # Esto crea la primera fila con los nombres de columnas
    writter.writeheader()
    
    # Escribir una fila con los datos de archivo csv
    # Cada diccionario debe tener claves que coincidan con los nombres de las columnas
    writter.writerow({"nombre":"ana","Edad":22,"Ciudad":"Ensenada"})
    
    # Escribir multiples filas de datos en el archivo csv
    writter.writerows([
        {"nombre" : "ana","Edad":22,"Ciudad":"Ensenada"},
        {"nombre" : "alma","Edad":27,"Ciudad":"Ensenada"}
    ])
    