#4. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a. La cantidad de valores ingresados negativos.
#b. La cantidad de valores ingresados positivos.
#c. La cantidad de múltiplos de 15.
#d. El valor acumulado de los números ingresados que son pares.

for x in range(1, 11):
    num = int(input("ingresar numeros1"))

if num < 0:
    print("es negativo")
if num > 0:
    print("es positivo")
if num %15 == 0:
    print("es multiplo de 15")
if num %2 == 0:
    print("la suma de todos los numeros es par")

