#6. De un operario se conoce su sueldo y los años de antigüedad. Se pide
#confeccionar un programa que lea los datos de entrada e informe:
#a. Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10
#años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
#b. Si el sueldo es inferior a 500 pero su antigüedad es menor a 10
#años, otorgarle un aumento de 5 %.
#c. Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin
#cambios.

sueldo = int(input("cuanto cobra? "))
años = int(input("cuantos años lleva en la empresa "))

if sueldo < 500 and años >= 10:
    aumento20 = (sueldo *20)/100
    print("el aumento de su sueldo es: ")
    print(aumento20) 

if sueldo < 500 and años < 10:
    aumento5 = (sueldo *5)/100
    print("el aumento de su sueldo es: ")
    print(aumento5) 

else:
    if sueldo >= 500:
        print("su sueldo es de")
        print(int(sueldo))
