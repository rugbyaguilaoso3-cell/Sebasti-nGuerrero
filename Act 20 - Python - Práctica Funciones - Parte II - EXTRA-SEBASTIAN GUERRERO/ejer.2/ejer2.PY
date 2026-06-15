"""
2. Desarrollar una aplicación que permita ingresar por teclado los nombres de
5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con
un precio menor igual al valor ingresado.
"""
def cargar_articulos(nombres, precios):
    for x in range(5):
        nombre = input("Ingrese nombre del articulo: ")
        precio = float(input("Ingrese precio: "))

        nombres.append(nombre)
        precios.append(precio)


def imprimir_articulos(nombres, precios):
    print("\nListado de articulos")
    for x in range(len(nombres)):
        print(nombres[x], precios[x])


def articulo_mayor_precio(nombres, precios):
    pos = 0

    for x in range(1, len(precios)):
        if precios[x] > precios[pos]:
            pos = x

    print("Articulo con mayor precio:", nombres[pos])


def articulos_menores(nombres, precios):
    importe = float(input("Ingrese un importe: "))

    print("Articulos con precio menor o igual:")
    for x in range(len(precios)):
        if precios[x] <= importe:
            print(nombres[x], precios[x])



nombres = []
precios = []

cargar_articulos(nombres, precios)
imprimir_articulos(nombres, precios)
articulo_mayor_precio(nombres, precios)
articulos_menores(nombres, precios)

       










   