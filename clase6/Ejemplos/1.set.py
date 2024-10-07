# Sesión de asistentes a un evento
# Crear un programa que administre una lista de asistentes a eventos sin permitir duplicados y 
# que realice operaciones entre dos listas.add()

# Crear conjuntos de invitados
invitados_viernes = {"Ana","Carlos","Pedro","Luis","Clara"}
invitados_sabado = {"Carlos","Luis","Sofia","Maria","Pedro"}

# Mostrar a los invitados únicos que asisten el viernes
print(f"Invitados de viernes: ´{invitados_viernes}")

# Mostrar a los invitados únicos que asisten el sábado
print(f"Invitados de sábado: ´{invitados_sabado}")

# Mostrar unión (quien asistió ambos días)
todos_asistentes = invitados_sabado | invitados_viernes
print(f"Asistentes de ambos días: ´{todos_asistentes}")

# Mostrar la intersección (quien asisitió al menos un día)
solo_viernes = invitados_viernes & invitados_sabado
print(f"Asistentes solo el viernes: ´{solo_viernes}")

# Mostrar la diferencia 
solo_viernes = invitados_viernes - invitados_sabado
print(f"Asistencia solo el viernes: ´{solo_viernes}")

# Agregar un nuevo invitado el sábado
invitados_sabado.add("Miguel")
print(f"Invitados del sábado después de agregar un nuevo invitado: ´{invitados_sabado}")

# Eliminar un invitado que canceló
invitados_sabado.remove("Maria")
print(f"Invitados del sábado después de eliminar un invitado: ´{invitados_sabado}")

# Comprobar si Ana asisitó el sábado
print(f"Ana asistió el sábado?: {'Ana' in invitados_sabado}")