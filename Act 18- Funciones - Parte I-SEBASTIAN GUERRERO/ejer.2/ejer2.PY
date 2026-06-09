"""
2. Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida.
"""




def mostrar(valor1,valor2,valor3):
 
     
    if valor1 < valor2 and valor1 < valor3:
        print("El número menor es:", valor1)
    elif valor2 < valor1 and valor2 < valor3:
        print("El número menor es:", valor2)
    if valor3 < valor2 and valor3 < valor1:
        print("El número menor es:", valor3)
    elif valor1 > valor2 and valor1 > valor3:
        print("El número mayor es:", valor1)
    if valor2 > valor1 and valor2 > valor3:
        print("El número mayor es:", valor2)
    elif valor3 > valor1 and valor3 > valor2:
        print("El número mayor es:", valor3)
    if valor1>valor2 and valor1<valor3 or valor1<valor2 and valor1<valor3:
        print("el valor del medio es:", valor2)
    elif valor2>valor1 and valor2<valor3 or valor2<valor1 and valor2<valor3:
        print("el valor del medio es:", valor2)
    else:
        print("el valor del medio es:", valor3)
    
def carga1():
    
    n1 = int(input("Cargar el primer valor: "))
    n2 = int(input("Cargar el segundo valor: "))
    n3 = int(input("Cargar el tercer valor: "))
    mostrar(n1,n2,n3)
carga1()


