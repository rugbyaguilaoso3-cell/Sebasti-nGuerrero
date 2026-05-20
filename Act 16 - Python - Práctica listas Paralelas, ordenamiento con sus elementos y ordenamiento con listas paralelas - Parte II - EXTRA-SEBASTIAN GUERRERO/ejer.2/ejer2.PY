"""
2. Una empresa registra los nombres de sus 5 vendedores y el total de ventas
realizadas por cada uno en un mes. Cargar los nombres y ventas en dos
vectores paralelos, ordenar los datos de mayor a menor según las ventas,
imprimir la lista ordenada con nombre y monto de la venta, e informar quien fue
el que menos vendió de los 5 empleados.
"""

nombres=[]
ventas=[]

for x in range(5):

    nombre=input("Ingrese vendedor:")
    venta=int(input("Ingrese ventas:"))

    nombres.append(nombre)
    ventas.append(venta)

for k in range(4):
    for x in range(4-k):

        if ventas[x]<ventas[x+1]:

            aux=ventas[x]
            ventas[x]=ventas[x+1]
            ventas[x+1]=aux

            aux=nombres[x]
            nombres[x]=nombres[x+1]
            nombres[x+1]=aux

print("Ventas ordenadas")

for x in range(5):
    print(nombres[x],ventas[x])

print("Menos vendió:")

print(nombres[4],ventas[4])

