"""1:
 Una ciudad inteligente cuenta con sensores que miden las partículas contaminantes
 de dióxido de carbono (CO2) en diferentes puntos geográficos.
 Crear un diccionario donde la Clave sea el nombre del barrio o estación de
 monitoreo (ej: "San Telmo") y el Valor sea una lista de flotantes que represente
 las últimas 3 lecturas de contaminación tomadas en el día.
 Desarrollar las siguientes funciones:
 1. Cargar sensores: Ingresar por teclado 3 estaciones de monitoreo y, para cada
    una, solicitar las 3 lecturas consecutivas de CO2 (en partes por millón - ppm).
 2. Reportar promedios: Calcular y mostrar el promedio de contaminación de cada barrio.
 3. Alerta ambiental: Mostrar en pantalla una alerta roja de "Protocolo de Emergencia"
    únicamente para las estaciones cuyo promedio de contaminación supere las 400 ppm."""


def ingresar():
    dispositivos = {}

    for numero in range(3):
        lugar = input(f"Ingrese el nombre de la estacion {numero + 1}: ")
        mediciones = []

        for registro in range(3):
            dato = float(
                input(
                    f"Ingrese la lectura {registro + 1} de CO2 para {lugar} (ppm): "
                )
            )
            mediciones.append(dato)

        dispositivos[lugar] = mediciones

    return dispositivos


def mostrar_promedios(dispositivos):
    resultados = {}

    for lugar in dispositivos:
        mediciones = dispositivos[lugar]
        total = 0

        for posicion in range(len(mediciones)):
            total = total + mediciones[posicion]

        media = total / len(mediciones)
        resultados[lugar] = media
        print("Promedio de", lugar, ":", media, "ppm")

    return resultados


def generar_alerta(resultados):
    print("Alertas Ambientales")
    for lugar in resultados:
        media = resultados[lugar]
        if media > 400:
            print("ALERTA ROJA (Protocolo de Emergencia) en:", lugar, "con", media, "ppm",)


dispositivos = ingresar()
resultados = mostrar_promedios(dispositivos)
generar_alerta(resultados)
