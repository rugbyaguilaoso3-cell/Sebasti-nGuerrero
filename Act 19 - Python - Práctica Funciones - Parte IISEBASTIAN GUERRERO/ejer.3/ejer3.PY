"""
3. Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos
debe retornar la suma de dichos valores. Debe tener tres parámetros por
defecto.
"""

def sumar(v1, v2, v3=0, v4=0, v5=0):
    return v1+v2+v3+v4+v5


print(sumar(10,20))
print(sumar(10,20,30))
print(sumar(10,20,30,40))
print(sumar(10,20,30,40,50))



