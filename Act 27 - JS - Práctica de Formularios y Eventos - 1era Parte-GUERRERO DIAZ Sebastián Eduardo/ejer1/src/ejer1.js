/*1. Crear un formulario con tres botones con las leyendas &quot;1&quot;, &quot;2&quot; y &quot;3&quot;.
Mostrar un mensaje indicando qué botón se presionó. */



let boton1 = document.getElementById("boton1");
let boton2 = document.getElementById("boton2");
let boton3 = document.getElementById("boton3");

let resultado = document.getElementById("resultado");

boton1.addEventListener("click", function() {
    resultado.textContent = "Presionaste el botón 1";
});

boton2.addEventListener("click", function() {
    resultado.textContent = "Presionaste el botón 2";
});

boton3.addEventListener("click", function() {
    resultado.textContent = "Presionaste el botón 3";
});