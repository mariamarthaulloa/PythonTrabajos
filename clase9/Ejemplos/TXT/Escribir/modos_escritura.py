# Los tres ejemplos de escritura (TXT)

# Modo "w": Sobreescribe el archivo
with open("modo_w.txt","w") as file:
    file.write("Este archivo fue sobreescrito por el modo w")
    file.write("Todo el contenido previo fue eliminado.")
print("archivo modo w.txt creado con éxito.")

# Modo "a": Agrega contenido al archivo ya existente
with open("modo_a.txt","a") as file:
    file.write("A este archivo se le agrego al final con a")
    file.write("Todo el contenido previo no fue eliminado.")
print("archivo modo_a.txt creado/modificado con éxito.")

# Modo "x": Crea un nuevo archivo
with open("modo_x.txt","x") as file:
    file.write("Este archivo fue creado con éxito usando x")
    file.write("Falla si ya existe el archivo.")
print("archivo modo_x.txt creado con éxito.") 