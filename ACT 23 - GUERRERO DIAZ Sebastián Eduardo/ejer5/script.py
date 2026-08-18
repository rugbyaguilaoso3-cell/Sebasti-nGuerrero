"""
Ejercicio 5: Gestión de Triaje en Guardia Médica (Prioridad)
Contexto: Un hospital atiende pacientes según la gravedad de su condición (Triaje), no
únicamente por orden de llegada. Los niveles de urgencia son: 1 (Normal), 2 (Moderado) y 3
(Crítico).
Consigna: La sala de espera se representa como una lista de registros sin diccionarios:
[[&quot;Paciente&quot;, Prioridad], ...]. Crear la función atender_siguiente(cola_espera) que seleccione
al próximo paciente en ser atendido.
Requisitos:
● Buscar al paciente que posea la prioridad más alta (mayor número).
● En caso de empate en la prioridad, se debe atender al primero que haya llegado a
la guardia (criterio FIFO).
● Eliminar al paciente seleccionado de la lista de espera y devolver un mensaje
indicando su nombre y nivel de urgencia.
Ejemplo de Entrada: [[&quot;Carlos&quot;, 1], [&quot;Ana&quot;, 3], [&quot;Roberto&quot;, 2], [&quot;Lucía&quot;, 3]] Salida
Esperada: Atiende primero a Ana (Nivel 3). Si se vuelve a llamar a la función,
la siguiente será Lucía (Nivel 3).
"""
def ingresar():
    lista_espera = [
    ["Carlos", 1],
    ["Ana", 3],
    ["Roberto", 2],
    ["Lucía", 3]
    ]

    return lista_espera


def atender_siguiente(lista_espera):

    indice = 0

    for posicion in range(len(lista_espera)):

        if lista_espera[posicion][1] > lista_espera[indice][1]:
            indice = posicion

    nombre = lista_espera[indice][0]
    urgencia = lista_espera[indice][1]

    lista_espera.pop(indice)

    return nombre, urgencia


lista_espera = ingresar()
nombre, urgencia = atender_siguiente(lista_espera)

print("Atiende a:", nombre)
print("Nivel de urgencia:", urgencia)
