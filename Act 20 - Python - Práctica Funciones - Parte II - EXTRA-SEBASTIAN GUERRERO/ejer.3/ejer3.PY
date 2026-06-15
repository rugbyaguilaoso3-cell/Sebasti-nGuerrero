"""
3. Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores
positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""


def cargar_lista():
    lista = []

    for x in range(10):
        valor = int(input("Ingrese un numero: "))
        lista.append(valor)

    return lista


def generar_listas(lista):
    positivos = []
    negativos = []

    for elemento in lista:
        if elemento >= 0:
            positivos.append(elemento)
        else:
            negativos.append(elemento)

    return positivos, negativos


def imprimir_lista(lista):
    for elemento in lista:
        print(elemento, end=" ")
    print()


numeros = cargar_lista()

positivos, negativos = generar_listas(numeros)

print("Lista de positivos")
imprimir_lista(positivos)

print("Lista de negativos")
imprimir_lista(negativos)

