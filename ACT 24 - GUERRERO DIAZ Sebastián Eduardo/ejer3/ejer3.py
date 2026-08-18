"""3:
 Un sistema de hogar inteligente monitorea qué electrodomésticos consumen más energía
 en cada habitación de la casa.
 Crear un diccionario donde la Clave sea el nombre del ambiente (ej: "Cocina", "Dormitorio")
 y el Valor sea una lista de tuplas, donde cada tupla represente un
 dispositivo activo y su consumo: [(nombre_dispositivo, consumo_watts)].
 Desarrollar las siguientes funciones:
 1. Cargar dispositivos: Solicitar la carga de 3 habitaciones. Para cada habitación,
    ingresar el nombre de los dispositivos activos y su consumo en Watts hasta que el
    operador decida no cargar más para ese ambiente.
 2. Consumo por habitación: Imprimir el listado de habitaciones y el consumo total
    en Watts acumulado en cada una de ellas.
 3. Dispositivo crítico: Buscar e informar el nombre del electrodoméstico que más
    energía consume de toda la casa (el valor máximo individual dentro de todas las
    listas del diccionario), indicando en qué habitación se encuentra.
"""

def ingresar():
    vivienda = {}

    for numero in range(3):
        habitacion = input(f"Ingrese el nombre de la habitacion {numero + 1}: ")
        aparatos = []

        continuar = "si"
        while continuar.lower() == "si":
            nombre_aparato = input(
                f"Ingrese el nombre del dispositivo para {habitacion}: "
            )
            gasto = float(
                input(f"Ingrese el consumo en Watts de {nombre_aparato}: ")
            )

            aparatos.append((nombre_aparato, gasto))

            continuar = input(
                "¿Desea ingresar otro dispositivo en esta habitacion? (si/no): "
            )

        vivienda[habitacion] = aparatos

    return vivienda


def consumo_por_habitacion(vivienda):
    print("Consumo por Habitacion")
    for habitacion in vivienda:
        aparatos = vivienda[habitacion]
        consumo_total = 0

        for posicion in range(len(aparatos)):
            aparato = aparatos[posicion]
            consumo_total = consumo_total + aparato[1]

        print("Habitacion:", habitacion, " Consumo Total:", consumo_total, "Watts")


def dispositivo_critico(vivienda):
    mayor_consumo = -1
    aparato_critico = ""
    habitacion_critica = ""

    for habitacion in vivienda:
        aparatos = vivienda[habitacion]

        for posicion in range(len(aparatos)):
            aparato = aparatos[posicion]
            nombre_aparato = aparato[0]
            gasto = aparato[1]

            if gasto > mayor_consumo:
                mayor_consumo = gasto
                aparato_critico = nombre_aparato
                habitacion_critica = habitacion

    if aparato_critico != "":
        print(
            "Dispositivo critico:", aparato_critico, "con", mayor_consumo, "Watts en la habitacion:", habitacion_critica,
        )


vivienda = ingresar()
consumo_por_habitacion(vivienda)
dispositivo_critico(vivienda)

