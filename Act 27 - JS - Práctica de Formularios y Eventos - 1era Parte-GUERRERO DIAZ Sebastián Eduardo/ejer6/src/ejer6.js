/* 6. Confeccionar una página que permita tomar un examen múltiple choice.
Se debe mostrar una pregunta y seguidamente un objeto SELECT con
las respuestas posibles. Al presionar un botón mostrar la cantidad de
respuestas correctas e incorrectas (Disponer 4 preguntas y sus
respectivos controles SELECT)*/
let pregunta1 = document.getElementById("pregunta1");
let pregunta2 = document.getElementById("pregunta2");
let pregunta3 = document.getElementById("pregunta3");
let pregunta4 = document.getElementById("pregunta4");

let boton = document.getElementById("corregir");
let resultado = document.getElementById("resultado");

boton.addEventListener("click", function() {

    let correctas = 0;
    let incorrectas = 0;

    if (pregunta1.value == "correcta") {
        correctas = correctas + 1;
    }
    else {
        incorrectas = incorrectas + 1;
    }

    if (pregunta2.value == "correcta") {
        correctas = correctas + 1;
    }
    else {
        incorrectas = incorrectas + 1;
    }

    if (pregunta3.value == "correcta") {
        correctas = correctas + 1;
    }
    else {
        incorrectas = incorrectas + 1;
    }

    if (pregunta4.value == "correcta") {
        correctas = correctas + 1;
    }
    else {
        incorrectas = incorrectas + 1;
    }

    resultado.textContent = "Correctas: " + correctas + " - Incorrectas: " + incorrectas;

});