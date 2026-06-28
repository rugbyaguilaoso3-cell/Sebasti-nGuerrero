
"""
1-
Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""



def cargar_lista():
    lista = []

    for x in range(5):
        numero = int(input("Ingrese un número: "))
        lista.append(numero)

    return lista


def mayor_menor(lista):
    mayor = lista[0]
    menor = lista[0]

    for x in range(1, len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]

        if lista[x] < menor:
            menor = lista[x]

    return mayor, menor


lista = cargar_lista()

mayor, menor = mayor_menor(lista)

print("Mayor:", mayor)
print("Menor:", menor)














































































