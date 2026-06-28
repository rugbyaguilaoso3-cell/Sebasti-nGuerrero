"""
4-
Un observatorio astronómico registra los descubrimientos de nuevos planetas
fuera del sistema solar.
 Diseñar un diccionario donde la Clave sea el nombre científico del
exoplaneta (ej: &quot;Kepler-22b&quot;) y el Valor sea una tupla con sus datos:
(distancia_anios_luz, tipo_de_atmosfera, es_habitable_booleano).
Desarrollar las siguientes funciones:
1. Cargar catálogo: Registrar por teclado la información de 4 exoplanetas
descubiertos.
2. Buscar exoplaneta: Permitir al usuario ingresar el nombre de un
exoplaneta por teclado. Si el exoplaneta se encuentra en el diccionario
(utilizando el operador in), mostrar todos sus detalles físicos y si reúne
condiciones de habitabilidad. De lo contrario, mostrar un cartel indicando:
&quot;El exoplaneta no figura en el catálogo actual&quot;.
3. Reportar Habitables: Mostrar en pantalla únicamente los nombres de los
exoplanetas cargados que fueron marcados como habitables.
"""


def cargar():
    planetas={}
    x=0
    while x<4:
        nombre=input("Ingrese el nombre del exoplaneta: ")
        distancia=float(input("Ingrese la distancia en años luz: "))
        atmosfera=input("Ingrese el tipo de atmosfera: ")
        habitable=input("Es habitable? (si/no): ")

        if habitable=="si":
            estado=True
        else:
            estado=False

        planetas[nombre]=(distancia,atmosfera,estado)
        x=x+1
    return planetas

def buscar(planetas):
    nombre=input("Ingrese el nombre del exoplaneta: ")

    if nombre in planetas:
        print("Distancia:",planetas[nombre][0])
        print("Atmosfera:",planetas[nombre][1])

        if planetas[nombre][2]==True:
            print("Es habitable")
        else:
            print("No es habitable")
    else:
        print("El exoplaneta no figura en el catálogo actual")

def habitables(planetas):
    print("Exoplanetas habitables")
    for nombre in planetas:
        if planetas[nombre][2]==True:
            print(nombre)


planetas=cargar()
buscar(planetas)
habitables(planetas)


