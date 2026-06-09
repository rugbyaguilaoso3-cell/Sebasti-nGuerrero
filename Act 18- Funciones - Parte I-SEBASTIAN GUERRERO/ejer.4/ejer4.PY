"""
4. Plantear una función que reciba un string en mayúsculas o minúsculas y
retorne la cantidad de letras `a``A`
"""

def calcular(cosa):

    cont = 0
    for i in range (len(cosa)):
        if cosa[i] == "a" or cosa[i] == "A":
            cont = cont +1

        print(f"la catidad de a y A en la palabra: {cosa} es de {cont}")




def cargar():
    string = input("ingresar texto que contenga a y A: ")
    calcular(string)
cargar()







