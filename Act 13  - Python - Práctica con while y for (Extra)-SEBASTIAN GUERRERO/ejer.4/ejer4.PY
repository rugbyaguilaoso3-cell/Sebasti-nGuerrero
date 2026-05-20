#4. Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos
#en el plano. Informar cuántos puntos se han ingresado en el primer, segundo, tercer y
#cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de
#puntos a procesar.



cantidad_puntos = int(input("Ingrese cantidad de puntos: "))

primer_cuadrante = 0
segundo_cuadrante = 0
tercer_cuadrante = 0
cuarto_cuadrante = 0

for i in range(cantidad_puntos):

    x = float(input("Ingrese coordenada x: "))
    y = float(input("Ingrese coordenada y: "))

    if x > 0 and y > 0:
        primer_cuadrante = primer_cuadrante + 1

    else:
        if x < 0 and y > 0:
            segundo_cuadrante = segundo_cuadrante + 1

        else:
            if x < 0 and y < 0:
                tercer_cuadrante = tercer_cuadrante + 1

            else:
                if x > 0 and y < 0:
                    cuarto_cuadrante = cuarto_cuadrante + 1

print("Primer cuadrante:", primer_cuadrante)
print("Segundo cuadrante:", segundo_cuadrante)
print("Tercer cuadrante:", tercer_cuadrante)
print("Cuarto cuadrante:", cuarto_cuadrante)

