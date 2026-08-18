"""Ejercicio 4: Algoritmo de Compresión de Texto (RLE)
Contexto: En telecomunicaciones se utiliza el algoritmo Run-Length Encoding (RLE) para
comprimir secuencias de caracteres repetidos y ahorrar ancho de banda.
Consigna: Escribir la función comprimir_rle(texto) que reciba una cadena de caracteres en
mayúsculas y devuelva su versión comprimida.
Requisitos:
● Contar las apariciones consecutivas de cada carácter.
● Construir una cadena resultante intercalando el carácter con su cantidad de
apariciones consecutivas.
Ejemplo de Entrada: &quot;AAABBCDDDD&quot; Salida Esperada: &quot;A3B2C1D4&quot;
"""

def ingresar():
    cadena = input("Ingrese el texto: ")
    return cadena


def comprimir_rle(cadena):

    salida = ""
    cantidad = 1

    for posicion in range(len(cadena) - 1):

        if cadena[posicion] == cadena[posicion + 1]:
            cantidad = cantidad + 1

        else:
            salida = salida + cadena[posicion] + str(cantidad)
            cantidad = 1

    salida = salida + cadena[len(cadena) - 1] + str(cantidad)

    return salida


cadena = ingresar()
salida = comprimir_rle(cadena)

print("Texto comprimido:", salida)
