"""
3. Se registran los nombres de 5 atletas y sus tiempos (en segundos) en una
carrera de 100 metros. El programa debe cargar los datos en dos vectores
paralelos, calcular y mostrar el promedio de los tiempos, mostrar el nombre del
atleta con mejor y peor tiempo, y mostrar los nombres de quienes superaron el
promedio.
"""

nombres=[]
tiempos=[]

suma=0

for x in range(5):

    nombre=input("Ingrese atleta:")
    tiempo=float(input("Ingrese tiempo:"))

    nombres.append(nombre)
    tiempos.append(tiempo)

    suma=suma+tiempo

promedio=suma/5

mejor=tiempos[0]
peor=tiempos[0]

for x in range(1,5):

    if tiempos[x]<mejor:
        mejor=tiempos[x]

    if tiempos[x]>peor:
        peor=tiempos[x]

print("Promedio:")
print(promedio)

print("Mejor tiempo")

for x in range(5):

    if tiempos[x]==mejor:
        print(nombres[x],tiempos[x])

print("Peor tiempo")

for x in range(5):

    if tiempos[x]==peor:
        print(nombres[x],tiempos[x])

print("Superaron el promedio")

for x in range(5):

    if tiempos[x]<promedio:
        print(nombres[x],tiempos[x])