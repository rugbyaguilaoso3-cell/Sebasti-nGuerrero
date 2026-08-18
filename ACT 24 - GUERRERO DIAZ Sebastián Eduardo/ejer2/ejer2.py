""" 2:
 En un videojuego multijugador en línea, los jugadores se agrupan en clanes o gremios
 para realizar misiones cooperativas.
 Diseñar un diccionario donde la Clave sea el nombre del Gremio (ej: "DragonesDeFuego")
 y el Valor sea una lista de cadenas con los nombres de los jugadores (nicknames) que lo integran.
 Desarrollar las siguientes funciones:
 1. Registrar gremios: Cargar por teclado 3 gremios. Para cada gremio, se debe
    preguntar cuántos integrantes posee para cargar sus respectivos nombres de
    usuario en la lista interna.
 2. Listar clanes: Mostrar los nombres de todos los gremios junto a la cantidad total
    de miembros que posee cada uno.
 3. Buscar jugador: Solicitar por teclado el nombre de un jugador y buscar en qué
    gremio está registrado. Informar el gremio encontrado o indicar si el jugador es
    "Solitario" (no pertenece a ningún clan)."""


def registrar():
    equipos = {}

    for numero in range(3):
        nombre_equipo = input(f"Ingrese el nombre del gremio {numero + 1}: ")
        cantidad = int(input(f"¿Cuantos integrantes tiene {nombre_equipo}?: "))
        jugadores = []

        for registro in range(cantidad):
            usuario = input(f"Ingrese el nickname del jugador {registro + 1}: ")
            jugadores.append(usuario)

        equipos[nombre_equipo] = jugadores

    return equipos


def mostrar_equipos(equipos):
    print("Listado de Gremios")
    for equipo in equipos:
        jugadores = equipos[equipo]
        print("Gremio:", equipo, " Cantidad de miembros:", len(jugadores))


def buscar_jugador(equipos):
    jugadorBuscado = input("Ingrese el nickname del jugador a buscar: ")
    encontrado = False

    for equipo in equipos:
        jugadores = equipos[equipo]

        for posicion in range(len(jugadores)):
            if jugadores[posicion] == jugadorBuscado:
                print("El jugador", jugadorBuscado, "pertenece al gremio:", equipo)
                encontrado = True

    if encontrado == False:
        print("El jugador", jugadorBuscado, "es Solitario (no pertenece a ningún clan).")


equipos = registrar()
mostrar_equipos(equipos)
buscar_jugador(equipos)


