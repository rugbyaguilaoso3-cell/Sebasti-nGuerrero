#1. En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
#realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos
#empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el
#programa deberá informar el importe que gasta la empresa en sueldos al personal.

 
cantidadempleados = int(input("Ingrese la cantidad de empleados: "))

entre100y300 = 0
mas300 = 0
totalsueldos = 0

for i in range(cantidadempleados):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i + 1}: "))

    if 100 <= sueldo <= 300:
        entre100y300 += 1
    elif sueldo > 300:
        mas300 += 1

    totalsueldos += sueldo

print("\nResultados:")
print("Empleados que cobran entre $100 y $300:", entre100y300)
print("Empleados que cobran más de $300:", mas300)



































































