"""
5-
Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada
elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15.
"""
def cargar():

    productos = []

    for x in range(5):

        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))

        productos.append((nombre, precio))

    return productos


def listar(productos):

    print("Lista de productos")

    for x in range(len(productos)):
        print(productos[x][0], "-", productos[x][1])


def entre_10_y_15(productos):

    print("Productos entre $10 y $15")

    for x in range(len(productos)):

        if productos[x][1] >= 10 and productos[x][1] <= 15:
            print(productos[x][0], "-", productos[x][1])



productos = cargar()

listar(productos)

entre_10_y_15(productos)