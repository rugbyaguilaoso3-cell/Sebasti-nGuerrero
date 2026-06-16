"""
2. Se desea saber la temperatura media trimestral de cuatro países. Para ello se
tiene como dato las temperaturas medias mensuales de dichos países. Se debe
ingresar el nombre del país y seguidamente las tres temperaturas medias
mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los
datos en memoria.

● Cargar por teclado los nombres de los países y las temperaturas
medias mensuales.
● Imprimir los nombres de los países y las temperaturas medias
mensuales de las mismas.
● Calcular la temperatura media trimestral de cada país.
● Imprimir los nombres de los países y las temperaturas medias
trimestrales.
● Imprimir el nombre del país con la temperatura media trimestral
mayor.
"""

paises = []

temperaturas = []


promedios = []


for x in range(4):
    nombre = input("Ingrese el nombre del país: ")
    paises.append(nombre)

    temp1 = float(input("Ingrese la temperatura del primer mes: "))
    temp2 = float(input("Ingrese la temperatura del segundo mes: "))
    temp3 = float(input("Ingrese la temperatura del tercer mes: "))

    temperaturas.append([temp1, temp2, temp3])


print("\nTemperaturas mensuales:")
for x in range(4):
    print("País:", paises[x])
    print("Temperaturas:", temperaturas[x][0], temperaturas[x][1], temperaturas[x][2])


for x in range(4):
    promedio = (temperaturas[x][0] +
                temperaturas[x][1] +
                temperaturas[x][2]) / 3
    promedios.append(promedio)


print("\nTemperaturas medias trimestrales:")
for x in range(4):
    print(paises[x], ":", promedios[x])


mayor = promedios[0]
posmayor = 0

for x in range(1, 4):
    if promedios[x] > mayor:
        mayor = promedios[x]
        posmayor = x

print("\nPaís con mayor temperatura media trimestral:")
print(paises[posmayor], "con", mayor)