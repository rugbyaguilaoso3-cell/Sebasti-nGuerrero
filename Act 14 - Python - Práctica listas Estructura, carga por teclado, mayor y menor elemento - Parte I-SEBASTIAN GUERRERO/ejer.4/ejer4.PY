"""
4. Cargar por teclado y almacenar en una lista las alturas de 5 personas
(valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más
altas que el promedio y cuántas más bajas.
"""



alturas=[]
suma=0

for x in range(5):

    altura=float(input("Ingrese altura:"))
    alturas.append(altura)

    suma=suma+altura

promedio=suma/5

altas=0
bajas=0

for x in range(5):

    if alturas[x]>promedio:
        altas=altas+1

    else:
        if alturas[x]<promedio:
            bajas=bajas+1

print("Promedio:")
print(promedio)

print("Más altas que el promedio:")
print(altas)

print("Más bajas que el promedio:")
print(bajas)
