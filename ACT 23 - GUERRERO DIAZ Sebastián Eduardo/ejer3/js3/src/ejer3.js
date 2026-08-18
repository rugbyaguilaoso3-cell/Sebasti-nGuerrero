/*Ejercicio 3: Tabla de Posiciones con Desempate (Listas Paralelas)
Contexto: Se está organizando un torneo deportivo y se necesita generar la tabla de
posiciones a partir de tres listas paralelas sincronizadas por índice: equipos, puntos y
diferencia_gol.
Consigna: Diseñar un algoritmo de ordenamiento que reorganice las tres listas de mayor a
menor según el desempeño de cada equipo.
Requisitos:
● Criterio Principal: Mayor cantidad de puntos.
● Criterio de Desempate: Si dos o más equipos empatan en puntos, la posición se
define por el equipo que tenga la mayor diferencia de gol.
● Mantener la sincronización perfecta entre las tres listas al realizar los intercambios.
Ejemplo de Entrada: equipos = [&quot;Boca&quot;, &quot;River&quot;, &quot;Racing&quot;] puntos = [12, 15, 12]
diferencia_gol = [8, 5, 10] Salida Esperada: 1° River (15 pts), 2° Racing (12 pts,
DG 10), 3° Boca (12 pts, DG 8). */

function carga(){
    let equipos = ["River", "Boca", "Racing"];
    let puntos = [12, 15, 12];
    let diferenciaGol = [8, 5, 10];

    return [equipos,puntos,diferenciaGol]
}
function ordenarTabla(equipos, puntos, diferenciaGol){

    for(let i=0; i<equipos.length; i++){

        for(let j=i+1; j<equipos.length; j++){

            if(puntos[j] > puntos[i]){

                let aux = equipos[i];
                equipos[i] = equipos[j];
                equipos[j] = aux;

                aux = puntos[i];
                puntos[i] = puntos[j];
                puntos[j] = aux;

                aux = diferenciaGol[i];
                diferenciaGol[i] = diferenciaGol[j];
                diferenciaGol[j] = aux;

            }else if(puntos[j] == puntos[i]){

                if(diferenciaGol[j] > diferenciaGol[i]){

                    let aux = equipos[i];
                    equipos[i] = equipos[j];
                    equipos[j] = aux;

                    aux = puntos[i];
                    puntos[i] = puntos[j];
                    puntos[j] = aux;

                    aux = diferenciaGol[i];
                    diferenciaGol[i] = diferenciaGol[j];
                    diferenciaGol[j] = aux;
                }
            }
        }
    }
}



let datos=carga()
let equipos=datos[0]
let puntos=datos[1]
let diferenciaGol=datos[2]
ordenarTabla(equipos, puntos, diferenciaGol);

for(let i=0; i<equipos.length; i++){
    console.log(i+1, "°", equipos[i], "-", puntos[i], "puntos - DG:", diferenciaGol[i]);
}