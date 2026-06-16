"""
4. Crear dos listas paralelas. En la primera ingresar los nombres de empleados y
en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la
empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el
sueldo como su nombre)
"""

empleados = []
sueldos = []

cantidad = int(input("Ingrese la cantidad de empleados: "))

for x in range(cantidad):
    nombre = input("Ingrese el nombre del empleado: ")
    empleados.append(nombre)

    sueldo = float(input("Ingrese el sueldo del empleado: "))
    sueldos.append(sueldo)

print("\nEmpleados y sus sueldos:")
for x in range(cantidad):
    print(empleados[x], "-", sueldos[x])


for x in range(cantidad - 1, -1, -1):
    if sueldos[x] > 10000:
        empleados.pop(x)
        sueldos.pop(x)

print("\nEmpleados restantes y sus sueldos:")
for x in range(len(empleados)):
    print(empleados[x], "-", sueldos[x])