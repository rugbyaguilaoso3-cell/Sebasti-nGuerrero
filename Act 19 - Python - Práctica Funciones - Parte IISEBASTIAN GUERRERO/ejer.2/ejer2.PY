"""
2. En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.
"""




def cargar_sueldos():
    sueldos=[]
    for x in range(10):
        sueldo=int(input("Ingrese sueldo: "))
        sueldos.append(sueldo)
    return sueldos

def imprimir_sueldos(lista):
    print("Lista de sueldos:")
    for x in range(len(lista)):
        print(lista[x])

def superiores_4000(lista):
    cantidad=0
    for x in range(len(lista)):
        if lista[x] > 4000:
            cantidad=cantidad+1
    print("Cantidad de sueldos superiores a 4000:", cantidad)

def promedio_sueldos(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    promedio=suma/len(lista)
    return promedio

def debajo_promedio(lista, promedio):
    print("Sueldos debajo del promedio:")
    for x in range(len(lista)):
        if lista[x] < promedio:
            print(lista[x])


sueldos=cargar_sueldos()

imprimir_sueldos(sueldos)

superiores_4000(sueldos)

prom=promedio_sueldos(sueldos)
print("Promedio:", prom)

debajo_promedio(sueldos, prom)


