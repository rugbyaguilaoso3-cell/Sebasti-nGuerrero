"""Ejercicio 2: Detector de Transacciones Sospechosas (Parseo)
Contexto: Un banco recibe un lote diario de movimientos en un único texto largo con el
formato &quot;ID:TIPO:MONTO&quot;, donde TIPO puede ser I (Ingreso) o E (Egreso), separados por
comas.
Consigna: Crear una función procesar_transacciones(cadena_texto) que reciba el texto de
movimientos y realice el procesamiento completo.
Requisitos:
● Parsear la cadena de texto separando cada registro.
● Calcular y retornar el balance total de la cuenta (Ingresos suman, Egresos restan).
● Generar y retornar una lista con los IDs de las transacciones consideradas
&quot;sospechosas&quot;. Una transacción es sospechosa si es un Egreso superior a
$50.000.
Ejemplo de Entrada: &quot;TX101:I:120000, TX102:E:15000, TX103:E:85000,
TX104:I:3000&quot; Salida Esperada:
● Balance final: $23.000
● Transacciones sospechosas: [&#39;TX103&#39;]"""

def ingresar():
    operaciones = input("Ingrese las transacciones: ")
    return operaciones


def analizar_transacciones(operaciones):

    movimientos = operaciones.split(",")

    saldo = 0
    alertas = []

    for posicion in range(len(movimientos)):

        informacion = movimientos[posicion].strip().split(":")

        identificador = informacion[0]
        categoria = informacion[1]
        valor = int(informacion[2])

        if categoria == "I":
            saldo = saldo + valor
        else:
            saldo = saldo - valor

            if valor > 50000:
                alertas.append(identificador)

    return saldo, alertas


def mostrar_resultado(saldo, alertas):
    print("Balance final:", saldo)
    print("Transacciones sospechosas:")

    for posicion in range(len(alertas)):
        print(alertas[posicion])


operaciones = ingresar()
saldo, alertas = analizar_transacciones(operaciones)
mostrar_resultado(saldo, alertas)
