"""
4-
Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en el primer componente el nombre del candidato y en la
segunda componente cargar una lista con componentes de tipo tupla con el
nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado.
1) Función para cargar todos los candidatos, sus nombres y las provincias con los
votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas
las provincias.
"""

def cargar():

    candidatos = []

    for x in range(3):

        nombre = input("Nombre del candidato: ")

        provincias = []

        for i in range(3):

            provincia = input("Provincia: ")
            votos = int(input("Votos: "))

            provincias.append((provincia, votos))

        candidatos.append([nombre, provincias])

    return candidatos


def imprimir_totales(candidatos):

    for x in range(len(candidatos)):

        total = 0

        for i in range(len(candidatos[x][1])):

            total = total + candidatos[x][1][i][1]

        print(candidatos[x][0], "obtuvo", total, "votos")




candidatos = cargar()

imprimir_totales(candidatos)






