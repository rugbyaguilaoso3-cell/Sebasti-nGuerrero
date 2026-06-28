
"""
1-
Crear un diccionario en Python que defina como clave el número de documento de
una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento.
"""


def cargar():
    personas={}
    x=0
    while x<4:
        dni=int(input("Ingrese el DNI: "))
        nombre=input("Ingrese el nombre: ")
        personas[dni]=nombre
        x=x+1
    return personas

def listado(personas):
    print("Listado completo")
    for dni in personas:
        print(dni, personas[dni])

def consulta(personas):
    dni=int(input("Ingrese el DNI a consultar: "))
    if dni in personas:
        print("Nombre:", personas[dni])
    else:
        print("No existe ese DNI")


personas=cargar()
listado(personas)
consulta(personas)













































































