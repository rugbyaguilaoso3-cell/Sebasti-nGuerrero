"""
3. Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los
números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltan menos
días.
"""

empleados = []


inasistencias = []


for x in range(3):
    nombre = input("Ingrese el nombre del empleado: ")
    empleados.append(nombre)

    cantidad = int(input("¿Cuántos días faltó?: "))

    inasistencias.append([])

    for k in range(cantidad):
        dia = int(input("Ingrese el día de inasistencia: "))
        inasistencias[x].append(dia)


print("\nListado de empleados y días de inasistencia")

for x in range(3):
    print("Empleado:", empleados[x])

    if len(inasistencias[x]) == 0:
        print("No tuvo inasistencias")
    else:
        print("Días que faltó:")

        for k in range(len(inasistencias[x])):
            print(inasistencias[x][k])


print("\nCantidad de inasistencias por empleado")

for x in range(3):
    print(empleados[x], "faltó", len(inasistencias[x]), "días")


menor = len(inasistencias[0])

for x in range(1, 3):
    if len(inasistencias[x]) < menor:
        menor = len(inasistencias[x])


print("\nEmpleado/s con menor cantidad de inasistencias:")

for x in range(3):
    if len(inasistencias[x]) == menor:
        print(empleados[x], "con", menor, "inasistencias")