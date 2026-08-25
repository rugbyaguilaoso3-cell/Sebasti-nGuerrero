/*
Ejercicio 04: Lista de Compras Dinámica

Confeccionar una página con un campo de texto y un botón “Agregar”.
Cada vez que se presione el botón, el producto ingresado en el campo debe añadirse
a una lista (&lt;ul&gt;).
Además:
 La lista debe permitir eliminar un producto haciendo clic sobre él.
 En consola debe mostrarse en todo momento la cantidad de productos
actuales en la lista.
*/
let producto = document.getElementById("producto");
let boton = document.getElementById("agregar");
let lista = document.getElementById("lista");

boton.addEventListener("click", function() {

    let elemento = document.createElement("li");

    elemento.textContent = producto.value;

    lista.appendChild(elemento);

    elemento.addEventListener("click", function() {
        elemento.remove();

        console.log("Cantidad de productos:", lista.children.length);
    });

    console.log("Cantidad de productos:", lista.children.length);

    producto.value = "";
});