"""
3-

Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista
con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en
una tupla)
El programa debe tener las siguientes funciones:
1)Carga de los nombres de empleados y sus últimos tres sueldos.
2)Imprimir el monto total cobrado por cada empleado.
3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a
10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería ser
similar a:
empleados = [[&quot;juan&quot;,(2000,3000,4233)] , [&quot;ana&quot;,(3444,1000,5333)] , etc. ]
"""


def cargar():
    empleados = []

    for x in range(5):

        nombre = input("Nombre: ")

        sueldo1 = float(input("Primer sueldo: "))
        sueldo2 = float(input("Segundo sueldo: "))
        sueldo3 = float(input("Tercer sueldo: "))

        empleados.append([nombre, (sueldo1, sueldo2, sueldo3)])

    return empleados


def imprimir_totales(empleados):

    for x in range(len(empleados)):

        total = empleados[x][1][0] + empleados[x][1][1] + empleados[x][1][2]

        print(empleados[x][0], "cobró", total)


def mayores_10000(empleados):

    print("Empleados con ingreso mayor a 10000:")

    for x in range(len(empleados)):

        total = empleados[x][1][0] + empleados[x][1][1] + empleados[x][1][2]

        if total > 10000:
            print(empleados[x][0])



empleados = cargar()

imprimir_totales(empleados)

mayores_10000(empleados)


