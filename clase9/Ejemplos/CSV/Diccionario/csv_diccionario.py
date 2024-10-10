# Importar el m+odulo
import csv

# Abrimos el archivo csv en modo lectura
with open("archivo2.csv","r") as file:
    # Convierte cada fila en diccionario
    reader = csv.reader(file)
    
    # Iterar sobre cada fila del archivo csv
    for fila in reader:
        print(fila)