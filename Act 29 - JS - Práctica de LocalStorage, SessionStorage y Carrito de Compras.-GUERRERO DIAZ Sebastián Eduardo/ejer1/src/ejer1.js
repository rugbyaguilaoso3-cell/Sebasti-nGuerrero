



/*
Ejercicio 1: Guardar Preferencias de Usuario
Enunciado: Crear una función que guarde y recupere las preferencias de un usuario,
como su nombre y el color de fondo preferido, utilizando LocalStorage.
1. La función debe permitir al usuario ingresar su nombre y seleccionar su color
de fondo preferido desde una lista de opciones.
2. Los datos ingresados deben almacenarse en LocalStorage.
3. Cada vez que la página se recargue, las preferencias deben recuperarse de
LocalStorage y aplicarse automáticamente (mostrar el nombre del usuario y
cambiar el color de fondo).
*/


let nombre = document.getElementById("nombre");
let color = document.getElementById("color");
let guardar = document.getElementById("guardar");
let mensaje = document.getElementById("mensaje");


function guardarPreferencias() {

    localStorage.setItem("nombre", nombre.value);
    localStorage.setItem("color", color.value);

    aplicarPreferencias();
}


function aplicarPreferencias() {

    let nombreGuardado = localStorage.getItem("nombre");
    let colorGuardado = localStorage.getItem("color");

    if (nombreGuardado != null) {
        nombre.value = nombreGuardado;
        mensaje.textContent = "Bienvenido, " + nombreGuardado;
    }

    if (colorGuardado != null) {
        color.value = colorGuardado;
        document.body.style.backgroundColor = colorGuardado;
    }
}


guardar.addEventListener("click", function() {
    guardarPreferencias();
});


aplicarPreferencias();