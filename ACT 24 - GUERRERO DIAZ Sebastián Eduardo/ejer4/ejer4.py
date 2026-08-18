"""4:
 Una empresa de e-commerce utiliza drones autónomos para realizar entregas a domicilio
 y necesita rastrear las coordenadas geográficas de sus rutas de vuelo.
 Diseñar un diccionario donde la Clave sea el identificador único del dron (ej: "DRON-01")
 y el Valor sea una lista de tuplas que almacene las coordenadas de
 las paradas programadas: [(latitud, longitud)].
 Desarrollar las siguientes funciones:
 1. Cargar planes de vuelo: Ingresar la información de 3 drones. Solicitar para cada
    uno la cantidad de paradas que va a realizar y cargar sus respectivas coordenadas geográficas.
 2. Imprimir rutas: Mostrar el listado completo de los drones junto con sus paradas
    de coordenadas asociadas.
 3. Ruta más larga: Determinar y mostrar el identificador del dron que tiene la mayor
    cantidad de paradas registradas en su ruta de vuelo (la lista con mayor cantidad de elementos).
"""
def ingresar():
    vehiculos = {}

    for numero in range(3):
        codigo = input(
            f"Ingrese el identificador del dron {numero + 1} (ej: DRON-01): "
        )
        cantidad_paradas = int(
            input(f"¿Cuantas paradas realizara el {codigo}?: ")
        )
        recorrido = []

        for registro in range(cantidad_paradas):
            latitud = float(
                input(f"Ingrese la latitud de la parada {registro + 1}: ")
            )
            longitud = float(
                input(f"Ingrese la longitud de la parada {registro + 1}: ")
            )
            recorrido.append((latitud, longitud))

        vehiculos[codigo] = recorrido

    return vehiculos


def mostrar_rutas(vehiculos):
    print("Listado Completo de Rutas")
    for codigo in vehiculos:
        recorrido = vehiculos[codigo]
        print("Dron:", codigo)

        for posicion in range(len(recorrido)):
            coordenada = recorrido[posicion]
            print(
                "  Parada",
                posicion + 1,
                ": Latitud",
                coordenada[0],
                ", Longitud",
                coordenada[1],
            )


def recorrido_mas_largo(vehiculos):
    mayor_cantidad = -1
    codigo_mayor = ""

    for codigo in vehiculos:
        recorrido = vehiculos[codigo]

        if len(recorrido) > mayor_cantidad:
            mayor_cantidad = len(recorrido)
            codigo_mayor = codigo

    if codigo_mayor != "":
        print("El dron con la ruta mas larga es", codigo_mayor, "conn", mayor_cantidad, "paradas registradas.",)


vehiculos = ingresar()
mostrar_rutas(vehiculos)
recorrido_mas_largo(vehiculos)

