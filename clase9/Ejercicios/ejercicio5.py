# Ejercicio 5: Escribir en un archivo CSV

# Crea un programa que guarde los siguientes datos en un archivo CSV alumnos.csv: 
# ["Nombre", "Edad"], ["Ana", 23], ["Luis", 25].

import csv

with open('alumnos.csv', 'w', newline='') as file:
    nueva_linea = csv.writer(file)
    nueva_linea.writerow(["Nombre", "Edad"])
    nueva_linea.writerow(["Ana", 23])
    nueva_linea.writerow(["Luis", 25])