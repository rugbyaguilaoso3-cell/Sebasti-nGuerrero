
"""
1. Desarrollar una función que reciba una lista de string y nos retorne el que
tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres
debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))
(La lista debe tener la misma cantidad de elementos, pero los textos los
eligen ustedes)
"""

def mascaracteres(lista):
    mayor = lista[0]
    for palabra in lista:
        if len(palabra) > len(mayor):
            mayor = palabra
        elif len(palabra) == len(mayor):
            if palabra < mayor:
                mayor=palabra
    
    return mayor

palabras=["paralelepipedo", "ferrofluidoso", "pluscuamperfecto", "ayerfuemicumpleaños", "holacomoestas", "sebastianguerrero"]

print("palabra con mas caracteres: ", mascaracteres(palabras))
















































































