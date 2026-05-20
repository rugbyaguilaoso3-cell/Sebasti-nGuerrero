#2. Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la
#altura promedio de las personas.

suma=0
for x in range(1, 11):
    alturas = int(input("ingrese las alturas"))
    suma = alturas + suma
promedio = suma / 10
print("el promedio de alturas es:", promedio)


