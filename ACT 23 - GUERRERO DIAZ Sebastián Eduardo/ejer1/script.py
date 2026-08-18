"""Ejercicio 1: Sistema de Reserva de Butacas (Matrices 2D)
Contexto: Un cine necesita un módulo automatizado para vender entradas. La sala se
representa como una matriz (lista de listas) de N filas por M columnas, donde un 0
representa un asiento libre y un 1 uno ocupado.
Consigna:
Escribir una función llamada reservar_consecutivos(sala, fila, cantidad) que reciba la matriz
de la sala, el número de fila deseado y la cantidad de entradas que desea comprar el grupo
de clientes.
Requisitos:
● Debe buscar si existen suficientes asientos libres y contiguos (juntos) en esa
misma fila.
● Si los encuentra, debe cambiar sus valores a 1 (ocupados) y retornar un mensaje
confirmando la reserva con los números de columna asignados.
● Si no hay espacio consecutivo suficiente, debe indicar que no fue posible realizar la
reserva sin modificar la sala.
Ejemplo de Entrada:
Sala de 3x5. En la fila 0, la columna 1 ya está ocupada: [ [0, 1, 0, 0, 0], ... ]
Intentar reservar 3 asientos en la fila 0.
Salida Esperada: Confirmación de reserva para las columnas 2, 3 y 4."""

def iniciarReserva():
    butacas = [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 0, 1]
    ]

    entradas = int(input("¿Cuántas entradas quiere sacar? "))
    filaElegida = int(input("¿En qué fila? (1 al 5): ")) - 1

    return [butacas, filaElegida, entradas]


def buscarLugares(info):
    butacas = info[0]
    filaElegida = info[1]
    totalEntradas = info[2]

    libresSeguidos = 0

    for posicion in range(len(butacas[filaElegida])):

        if butacas[filaElegida][posicion] == 0:
            libresSeguidos = libresSeguidos + 1
        else:
            libresSeguidos = 0

        if libresSeguidos == totalEntradas:

            primerLugar = posicion - totalEntradas + 1
            lugares = []

            for lugar in range(primerLugar, posicion + 1):
                lugares.append(lugar)
                butacas[filaElegida][lugar] = 1

            print("Reserva realizada.")
            print("Las columnas asignadas son:", lugares)

            print("Estado actual de la sala:")
            for fila in butacas:
                print(fila)

            return

    print("No fue posible realizar la reserva.")


informacion = iniciarReserva()
buscarLugares(informacion)


