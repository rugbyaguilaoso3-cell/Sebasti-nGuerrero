"""
1. Se desea desarrollar un programa que permita registrar los nombres y las
calificaciones de 6 estudiantes. Luego de cargar los datos, se debe mostrar el
nombre del estudiante con la nota más alta, junto con su nota. Al igual que el
estudiante con la nota más baja. Informar si hay estudiantes con la misma nota
máxima o mínima.
"""
nombres=[]
notas=[]

for x in range(6):

    nombre=input("Ingrese nombre:")
    nota=int(input("Ingrese nota:"))

    nombres.append(nombre)
    notas.append(nota)

mayor=notas[0]
menor=notas[0]

for x in range(1,6):

    if notas[x]>mayor:
        mayor=notas[x]

    if notas[x]<menor:
        menor=notas[x]

print("Nota más alta")

for x in range(6):

    if notas[x]==mayor:
        print(nombres[x],notas[x])

print("Nota más baja")

for x in range(6):

    if notas[x]==menor:
        print(nombres[x],notas[x])

contmayor=0
contmenor=0

for x in range(6):

    if notas[x]==mayor:
        contmayor=contmayor+1

    if notas[x]==menor:
        contmenor=contmenor+1

if contmayor>=2:
    print("Hay notas máximas repetidas")

if contmenor>=2:
    print("Hay notas mínimas repetidas")
