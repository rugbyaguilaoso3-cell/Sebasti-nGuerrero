/*Ejercicio 2: Detector de Transacciones Sospechosas (Parseo)
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
● Transacciones sospechosas: [&#39;TX103&#39;] */

function ingresar(){
    let operaciones = prompt("Ingrese las transacciones");
    return operaciones
}

function analizarTransacciones(operaciones){

    let movimientos = operaciones.split(",");

    let saldo = 0;
    let alertas = [];

    for(let posicion=0; posicion<movimientos.length; posicion++){

        let informacion = movimientos[posicion].trim().split(":");

        let identificador = informacion[0];
        let categoria = informacion[1];
        let valor = parseInt(informacion[2]);

        if(categoria == "I"){
            saldo = saldo + valor;
        }else{

            saldo = saldo - valor;

            if(valor > 50000){
                alertas.push(identificador);
            }
        }
    }

    return [saldo, alertas];
}


function mostrarResultado(saldo, alertas){
console.log("Balance final:", saldo);
console.log("Transacciones sospechosas:");

for(let posicion=0; posicion<alertas.length; posicion++){
    console.log(alertas[posicion]);
}
}

let operaciones=ingresar()

let resultado = analizarTransacciones(operaciones);
let saldo = resultado[0];
let alertas = resultado[1];

mostrarResultado(saldo, alertas)
