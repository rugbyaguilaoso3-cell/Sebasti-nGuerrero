#7. Escribir un programa en el cual: dada una lista de tres valores numéricos
#distintos se calcule e informe su rango de variación (debe mostrar el mayor
#y el menor de ellos)

num1 = int(input("cargar el primer numero: "))
num2 = int(input("cargar el segundo numero: "))
num3 = int(input("cargar el tercero numero: "))

mayor = num1
menor = num1

if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3

if num2 < mayor:
    menor = num2
if num3 < mayor:
    menor = num3


print(" el valor mayor")
print(mayor)
print(" el valor menor")
print(menor)
    