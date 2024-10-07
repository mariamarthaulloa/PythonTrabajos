# Ejercicio 10: Buscar y Actualizar la Información en un Diccionario Anidado

#1. Crea un diccionario que represente una base de datos de empleados de una empresa. El diccionario debe tener:
#o nombre_empresa
#o empleados, que es una lista de diccionarios

empleados = {
    "nombre_empresa":"Aearo",
    "empleados": [
        {"id_empleado":1888, "nombre":"Pablo", "departamento":"Ingenieria","Salario":4555},
        {"id_empleado":1856, "nombre":"Pedro", "departamento":"Informatica","Salario":4745},
        {"id_empleado":1488, "nombre":"Sebastian", "departamento":"RH","Salario":4458}
    ]
}

#2. Escribe una función que busque y actualice el salario de un empleado dado su id_empleado. La función debe:
#o Buscar el empleado por su id_empleado.
#o Actualizar el salario del empleado a un nuevo valor proporcionado.
#o Imprimir la información del empleado después de la actualización.

def actualizar_salario(empleados, id_empleado, nuevo_salario):
    for empleado in empleados["empleados"]:
        if empleado["id_empleado"] == id_empleado:
            empleado["Salario"] = nuevo_salario
            print(f"Empleado actualizado: {empleado}")
            return  # Termina la función después de actualizar
    print("Empleado no encontrado")

# Ejemplo: vamos a actualizar el salario de Pedro:
actualizar_salario(empleados, 1856, 5000)
