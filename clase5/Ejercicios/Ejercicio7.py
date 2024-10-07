#Ejercicio 7: Contar Ocurrencias de Elementos en un Diccionario Anidado

# 1. Crea un diccionario que contenga información sobre tres clubes deportivos, cada uno con una lista de jugadores.
#o Cada jugador es un diccionario con las claves: nombre y edad.

# Diccionario de clubes deportivos
clubes = {
    "Club Tierra": [
        {"nombre": "Martha",
         "edad": 24},
        {"nombre": "Armando",
         "edad": 28},
        {"nombre": "Zarina",
         "edad": 22}],
    "Club BajaMar": [
        {"nombre": "Carlos", 
         "edad": 33},
        {"nombre": "Pablo", 
         "edad": 30}],
    "Club CaliBaja": [
        {"nombre": "Loreto", 
         "edad": 16},
        {"nombre": "Raliz", 
         "edad": 28},
        {"nombre": "Mariel",
         "edad": 33},
        {"nombre": "Conrado", 
         "edad": 24}
    ]
}

#2. Cuenta cuántos jugadores en total tienen cada uno de los clubes
for club, jugadores in clubes.items():
    print(f"{club} tiene {len(jugadores)} jugadores.")
