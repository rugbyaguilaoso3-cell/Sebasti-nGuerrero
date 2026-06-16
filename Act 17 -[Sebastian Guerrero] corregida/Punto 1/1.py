"""
1. Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego cambiar de elemento todos los enteros mayores a 50 del
primer elemento de &quot;lista&quot;. El resto de enteros menores a 50 deben encontrarse
en una nueva posición dentro de la lista.
Volver a imprimir la lista.
"""
lista = [[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print("Lista original:")
print(lista)

mayores = []
nueva_lista = []

for sublista in lista:
    menores = []

    for numero in sublista:
        if numero > 50:
            mayores.append(numero)
        else:
            menores.append(numero)

    nueva_lista.append(menores)

nueva_lista[0] = mayores

print("Lista modificada:")
print(nueva_lista)