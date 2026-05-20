"""
4. Se realiza una evaluación a 6 docentes por parte de sus alumnos. Se registran
sus nombres y puntajes promedio obtenidos (de 1 a 10).
Cargar sus datos en vectores paralelos, mostrar docente con calificación más
alta y más baja, ordenar los vectores de mayor a menor de acuerdo con la
calificación y mostrar en pantalla la cantidad de docentes que aprobaron y
desaprobaron (tomando como base que se aprueba con una nota mayor o
igual a 6)
"""
docentes=[]
notas=[]

for x in range(6):

    nombre=input("Ingrese docente:")
    nota=int(input("Ingrese calificación:"))

    docentes.append(nombre)
    notas.append(nota)

mayor=notas[0]
menor=notas[0]

for x in range(1,6):

    if notas[x]>mayor:
        mayor=notas[x]

    if notas[x]<menor:
        menor=notas[x]

print("Mayor calificación")

for x in range(6):

    if notas[x]==mayor:
        print(docentes[x],notas[x])

print("Menor calificación")

for x in range(6):

    if notas[x]==menor:
        print(docentes[x],notas[x])

for k in range(5):
    for x in range(5-k):

        if notas[x]<notas[x+1]:

            aux=notas[x]
            notas[x]=notas[x+1]
            notas[x+1]=aux

            aux=docentes[x]
            docentes[x]=docentes[x+1]
            docentes[x+1]=aux

print("Ordenados")

for x in range(6):
    print(docentes[x],notas[x])

aprobados=0
desaprobados=0

for x in range(6):

    if notas[x]>=6:
        aprobados=aprobados+1

    else:
        desaprobados=desaprobados+1

print("Aprobados:")
print(aprobados)

print("Desaprobados:")
print(desaprobados)