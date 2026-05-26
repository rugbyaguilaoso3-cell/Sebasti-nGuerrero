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
menores = []

for n in lista[0]:
    if n > 50:
        mayores.append(n)
    else:
        menores.append(n)


lista[0] = mayores


lista.append(menores)

print("Lista modificada:")
print(lista)