/* 2. Cargar un nombre y un apellido en dos text. Al presionar un botón,
concatenarlos y mostrarlos en un tercer text (Tener en cuenta que
podemos modificar la propiedad value de un objeto TEXT cuando ocurre
un evento). */

let nombre = document.getElementById("nombre");
let apellido = document.getElementById("apellido");

let boton = document.getElementById("boton");
let resultado = document.getElementById("resultado");

boton.addEventListener("click", function() {

    resultado.value = nombre.value + " " + apellido.value;

});