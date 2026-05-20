#3. Realizar un programa que permita cargar dos listas de 15 valores cada una.
#Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor
#(mensajes &quot;Lista 1 mayor&quot;, &quot;Lista 2 mayor&quot;, &quot;Listas iguales&quot;) Tener en cuenta que
#puede haber dos o más estructuras repetitivas en un algoritmo.
suma_lista1 = 0
suma_lista2 = 0

print("Carga de la lista 1")

for i in range(15):

    valor = int(input("Ingrese valor: "))
    suma_lista1 = suma_lista1 + valor

print("Carga de la lista 2")

for i in range(15):

    valor = int(input("Ingrese valor: "))
    suma_lista2 = suma_lista2 + valor

if suma_lista1 > suma_lista2:
    print("Lista 1 mayor")

else:
    if suma_lista2 > suma_lista1:
        print("Lista 2 mayor")
    else:
        print("Listas iguales")
