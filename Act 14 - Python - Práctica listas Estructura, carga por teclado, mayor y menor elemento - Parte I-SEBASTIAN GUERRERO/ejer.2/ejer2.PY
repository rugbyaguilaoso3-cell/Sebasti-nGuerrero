"""
2. Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8
empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa
que permita almacenar los sueldos de los empleados agrupados en dos
listas. Imprimir las dos listas de sueldos.
"""

mañana=[]
tarde=[]

print("Turno mañana")

for x in range(4):
    sueldo=int(input("Ingrese sueldo:"))
    mañana.append(sueldo)

print("Turno tarde")

for x in range(4):
    sueldo=int(input("Ingrese sueldo:"))
    tarde.append(sueldo)

print("Sueldos turno mañana")
print(mañana)

print("Sueldos turno tarde")
print(tarde)

