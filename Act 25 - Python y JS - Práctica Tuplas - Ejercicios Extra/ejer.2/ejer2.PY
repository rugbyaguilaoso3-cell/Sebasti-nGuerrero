"""
2-
Para un sistema de radares de tránsito, se necesita registrar la ubicación geográfica de 4
cámaras de control.
 Almacenar en una lista las coordenadas de las 4 cámaras. Cada elemento de la
lista debe ser una tupla de dos flotantes (latitud, longitud) ingresados por teclado.
Desarrollar las siguientes funciones:
1. Cargar coordenadas: Solicitar la latitud y la longitud de cada una de las 4
cámaras para armar las tuplas y agregarlas a la lista.
2. Listar posiciones: Recibir la lista e imprimir las coordenadas de todas las
cámaras. Importante: Realizar el recorrido utilizando un bucle for que
desempaquete la tupla directamente en las variables lat y lon en cada vuelta (sin
utilizar índices numéricos como [0] o [1]).
3. Filtrar hemisferio: Contar e informar cuántas de las cámaras se encuentran
ubicadas en el hemisferio norte (latitud mayor a cero).
"""
def cargar_coordenadas():
    coordenadas = []

    for i in range(4):
        latitud = float(input("Ingrese la latitud: "))
        longitud = float(input("Ingrese la longitud: "))

        coordenadas.append((latitud, longitud))

    return coordenadas
def listar_posiciones(coordenadas):

    for lat, lon in coordenadas:
        print("Latitud:", lat, "Longitud:", lon)

def filtrar_hemisferio(coordenadas):

    cantidad = 0

    for lat, lon in coordenadas:
        if lat > 0:
            cantidad = cantidad + 1

    print("Cantidad de cámaras en el hemisferio norte:", cantidad)




coordenadas = cargar_coordenadas()

listar_posiciones(coordenadas)

filtrar_hemisferio(coordenadas)