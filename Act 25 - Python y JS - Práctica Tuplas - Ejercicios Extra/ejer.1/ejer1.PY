
"""
1-
Confeccionar un programa que permita registrar las temperaturas máximas de las últimas
6 horas en una lista.
Desarrollar las siguientes funciones:
1. Carga: Solicitar al operador el ingreso por teclado de las 6 temperaturas y
almacenarlas en una lista.
2. Procesar Extremos: Recibir la lista como parámetro y retornar una tupla que
contenga en su primer componente el valor máximo y en el segundo el valor
mínimo.
3. Bloque Principal: Desempaquetar la tupla devuelta por la función anterior en dos
variables individuales (máxima y mínima) y mostrarlas en pantalla con un mensaje
descriptivo.
"""
def cargar():
    temperaturas = []
    for i in range(6):
        temperatura = float(input("ingrese la temperatura: "))
        temperaturas.append(temperatura)
    return temperaturas
def procesar_extremos(temperaturas):
    maxima=temperaturas[0]
    minima=temperaturas[0]
    for i in range (1,len(temperaturas)):
        if temperaturas[i]>maxima:
            maxima=temperaturas[i] 
        if temperaturas[i]<minima:
            minima= temperaturas[i]
    tupla= (maxima, minima)
    return tupla
temperaturas = cargar()
maxima, minima =procesar_extremos(temperaturas)
print("temperatura maxima: ", maxima)
print("temperatura minima: ", minima)














































































