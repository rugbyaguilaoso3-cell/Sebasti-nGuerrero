/* Ejercicio 1: Sistema de Reserva de Butacas (Matrices 2D)
Contexto: Un cine necesita un módulo automatizado para vender entradas. La sala se
representa como una matriz (lista de listas) de N filas por M columnas, donde un 0
representa un asiento libre y un 1 uno ocupado.
Consigna:
Escribir una función llamada reservar_consecutivos(sala, fila, cantidad) que reciba la matriz
de la sala, el número de fila deseado y la cantidad de entradas que desea comprar el grupo
de clientes.
Requisitos:
● Debe buscar si existen suficientes asientos libres y contiguos (juntos) en esa
misma fila.
● Si los encuentra, debe cambiar sus valores a 1 (ocupados) y retornar un mensaje
confirmando la reserva con los números de columna asignados.
● Si no hay espacio consecutivo suficiente, debe indicar que no fue posible realizar la
reserva sin modificar la sala.
Ejemplo de Entrada:
Sala de 3x5. En la fila 0, la columna 1 ya está ocupada: [ [0, 1, 0, 0, 0], ... ]
Intentar reservar 3 asientos en la fila 0.
Salida Esperada: Confirmación de reserva para las columnas 2, 3 y 4.*/

function iniciarReserva() {
    let butacas = [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 0, 1]
    ];

    let entradas = parseInt(prompt("¿Cuántas entradas quiere sacar?"));
    let filaElegida = parseInt(prompt("¿En qué fila? (1 al 5): ")) - 1;

    return [butacas, filaElegida, entradas];
}

function buscarLugares(info) {
    let butacas = info[0];
    let filaElegida = info[1];
    let totalEntradas = info[2];

    let libresSeguidos = 0;

    for (let posicion = 0; posicion < butacas[filaElegida].length; posicion++) {

        if (butacas[filaElegida][posicion] == 0) {
            libresSeguidos = libresSeguidos + 1;
        } else {
            libresSeguidos = 0;
        }

        if (libresSeguidos == totalEntradas) {

            let primerLugar = posicion - totalEntradas + 1;
            let lugares = [];

            for (let lugar = primerLugar; lugar <= posicion; lugar++) {
                lugares.push(lugar);
                butacas[filaElegida][lugar] = 1;
            }

            console.log("Reserva realizada.");
            console.log("Las columnas asignadas son:", lugares);

            console.log("Estado actual de la sala:");
            for (let fila of butacas) {
                console.log(fila);
            }

            return;
        }
    }

    console.log("No fue posible realizar la reserva.");
}

let informacion = iniciarReserva();
buscarLugares(informacion);


