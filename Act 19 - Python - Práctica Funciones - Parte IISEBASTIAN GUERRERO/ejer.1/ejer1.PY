
"""
1. Crear una lista de enteros por asignación. Definir una función que reciba
una lista de enteros y un segundo parámetro de tipo entero. Dentro de la
función mostrar cada elemento de la lista multiplicado por el valor entero
enviado.
lista=[3, 7, 8, 10, 2]
multiplicar(lista,3)
"""


def multiplicar(lista, numero):
    for x in range(len(lista)):
        print(lista[x] * numero)


lista=[3,7,8,10,2]
multiplicar(lista,3)

