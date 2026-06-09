
"""
1. Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha
función (sin utilizar una estructura repetitiva)
"""


def solicitar():
    
    valor1 = int(input("Cargar el primer valor: "))
    valor2 = int(input("Cargar el segundo valor: "))
    valor3 = int(input("Cargar el tercer valor: "))

    
    if valor1 < valor2 and valor1 < valor3:
        print("El número menor es:", valor1)
    elif valor2 < valor1 and valor2 < valor3:
        print("El número menor es:", valor2)
    else:
        print("El número menor es:", valor3)
        
    



solicitar()
solicitar()

