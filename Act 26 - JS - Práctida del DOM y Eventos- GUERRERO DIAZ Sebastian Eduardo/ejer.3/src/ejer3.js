
/*
Ejercicio 03: Simulador de Votación en Línea
Plantear una página con 3 botones, cada uno representando un candidato distinto.
Al hacer clic en uno de los botones, se deberá aumentar el contador de votos de ese
candidato y mostrar el total actualizado en pantalla.
Además:
 El sistema debe mostrar en consola quién va ganando cada vez que se registra
un voto.
 Si hay un empate, debe mostrar el mensaje “Hay un empate”.
 */
let boton1 = document.getElementById("candidato1");
let boton2 = document.getElementById("candidato2");
let boton3 = document.getElementById("candidato3");

let votos1 = document.getElementById("votos1");
let votos2 = document.getElementById("votos2");
let votos3 = document.getElementById("votos3");

let resultado = document.getElementById("resultado");

let contador1 = 0;
let contador2 = 0;
let contador3 = 0;


function mostrarGanador() {

    if (contador1 > contador2 && contador1 > contador3) {
        console.log("Va ganando Candidato 1");
        resultado.textContent = "Va ganando Candidato 1";
    }
    else if (contador2 > contador1 && contador2 > contador3) {
        console.log("Va ganando Candidato 2");
        resultado.textContent = "Va ganando Candidato 2";
    }
    else if (contador3 > contador1 && contador3 > contador2) {
        console.log("Va ganando Candidato 3");
        resultado.textContent = "Va ganando Candidato 3";
    }
    else {
        console.log("Hay un empate");
        resultado.textContent = "Hay un empate";
    }
}


boton1.addEventListener("click", function() {

    contador1 = contador1 + 1;
    votos1.textContent = contador1;

    mostrarGanador();
});


boton2.addEventListener("click", function() {

    contador2 = contador2 + 1;
    votos2.textContent = contador2;

    mostrarGanador();
});


boton3.addEventListener("click", function() {

    contador3 = contador3 + 1;
    votos3.textContent = contador3;

    mostrarGanador();
});