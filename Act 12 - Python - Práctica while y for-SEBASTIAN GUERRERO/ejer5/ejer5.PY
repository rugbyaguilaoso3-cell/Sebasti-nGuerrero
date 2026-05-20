#5. Realizar un programa que lea los lados de n triángulos, e informar:
#a. De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados
#iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
#b. Cantidad de triángulos de cada tipo.

equilateros = 0
isosceles = 0
escalenos = 0

n = int(input("Ingrese la cantidad de triángulos: "))

for x in range(1, n + 1):
    print("Triángulo número:",x)
    l1 = float(input("Lado 1: "))
    l2 = float(input("Lado 2: "))
    l3 = float(input("Lado 3: "))

    
    if l1 == l2 == l3:
        print("Es equilátero")
        equilateros = equilateros + 1
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Es isósceles")
        isosceles = isosceles + 1
    else:
        print("Es escaleno")
        escalenos = escalenos + 1

print("\n--- Resultados ---")
print("Equiláteros:", equilateros)
print("Isósceles:", isosceles)
print("Escalenos:", escalenos)





























