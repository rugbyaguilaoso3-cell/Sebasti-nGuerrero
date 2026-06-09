"""
3. Confeccionar una función que calcule la superficie de un rectángulo y la
retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y
luego mostrar cuál de los dos tiene una superficie mayor.
"""

def retornar_superficie(valor1,valor2,lado1,lado2):

    superficie1 = valor1 * valor2
    print("la superficie del rectangulo n1 es: ", superficie1)
    superficie2 = lado1 * lado2
    print("la superficie del rectangulo n2 es: ", superficie2)

    if superficie1 > superficie2:
        print("la superficie del rectangulo n1 es mayor")
    else:
        print("la superficie del rectangulo n2 es mayor")

def cargar():
    lado1= int(input("cargar lado 1: "))
    lado2 = int(input("cargar lado 2: "))
    valor1 = int(input("cargar lado 3: "))
    valor2 = int(input("cargar lado 4: "))
    retornar_superficie(lado1,lado2,valor1,valor2)
cargar()



