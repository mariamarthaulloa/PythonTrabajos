# Crear una tupla con varios elementos
mi_tupla = (10,20,30,40,50)

# Encontrar la posición del número 30 en la Tupla
indice_de_30 = mi_tupla.index(30)

# Mostrar el resultado
print("El número 30 se encuentra en la posición, ",indice_de_30, "de la tupla")

# Verificar si un valor está en la tupla antes de buscar su índice
valor_buscado = 30

if valor_buscado in mi_tupla:
    # si el valor está en la tupla, encontrar su índice
    indice_del_valor = mi_tupla.index(valor_buscado)
    print(f"El número {valor_buscado} se encuentra en la posición {indice_del_valor} de la tupla")
else:
    #si el valor no está en la tupla, mostrar un mensaje
    print(f"El número {valor_buscado} no está en la tupla.")