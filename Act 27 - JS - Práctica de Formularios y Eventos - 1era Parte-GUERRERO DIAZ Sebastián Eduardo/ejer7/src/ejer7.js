/* 7. Confeccionar una página que muestre tres checkbox que permitan
seleccionar los deportes que practica el usuario (Fútbol, Básquet, Tenis)
Mostrar al presionar un botón los deportes que eligió.*/


let futbol = document.getElementById("futbol");
let basquet = document.getElementById("basquet");
let tenis = document.getElementById("tenis");

let boton = document.getElementById("mostrar");
let resultado = document.getElementById("resultado");

boton.addEventListener("click", function() {

    let deportes = "";

    if (futbol.checked) {
        deportes = deportes + "Fútbol ";
    }

    if (basquet.checked) {
        deportes = deportes + "Básquet ";
    }

    if (tenis.checked) {
        deportes = deportes + "Tenis ";
    }

    resultado.textContent = "Deportes elegidos: " + deportes;

});