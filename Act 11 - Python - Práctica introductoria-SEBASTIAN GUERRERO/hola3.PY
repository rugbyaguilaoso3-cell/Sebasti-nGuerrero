#3. Realizar un programa que solicite la carga por teclado de dos números, si el
#primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la división del primero respecto al segundo.

num1 = int(input("cargar el primer numero "))
num2 = int(input("cargar el segundo numero "))

if num1 > num2:
    print ("suma")
    print (int(num1 + num2))
else :
    if num1 < num2:
        print ("multiplicación")
print (int(num1 * num2))
print ("división")
print ((num1 / num2))
