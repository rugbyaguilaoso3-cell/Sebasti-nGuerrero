/*
Ejercicio 3: Borrador de Notas de Sesión
Enunciado: Crear una aplicación de notas rápidas que permita al usuario escribir un
mensaje o nota en un campo de texto y guardarlo de forma temporal utilizando
SessionStorage.
 Debe contar con un campo de texto (&lt;textarea&gt; o &lt;input&gt;) y un botón &quot;Guardar
Nota&quot;.
 Al hacer clic en el botón &quot;Guardar Nota&quot;, el texto ingresado debe almacenarse
en SessionStorage y mostrarse en un elemento dentro del DOM (por ejemplo,
en un contenedor &lt;div&gt; o párrafo).
 Al recargar la página (F5), la nota guardada debe recuperarse de
SessionStorage y seguir mostrándose en pantalla.
 Debe incluir un botón &quot;Borrar Nota&quot; que elimine el registro de SessionStorage
mediante removeItem() y limpie el contenido del DOM.
*/


let nota = document.getElementById("nota");
let guardar = document.getElementById("guardar");
let borrar = document.getElementById("borrar");
let mostrar = document.getElementById("mostrar");


function mostrarNota() {

    let notaGuardada = sessionStorage.getItem("nota");

    if (notaGuardada != null) {
        nota.value = notaGuardada;
        mostrar.textContent = notaGuardada;
    }
}


function guardarNota() {

    sessionStorage.setItem("nota", nota.value);

    mostrar.textContent = nota.value;
}


function borrarNota() {

    sessionStorage.removeItem("nota");

    nota.value = "";
    mostrar.textContent = "";
}


guardar.addEventListener("click", function() {
    guardarNota();
});

borrar.addEventListener("click", function() {
    borrarNota();
});


mostrarNota();