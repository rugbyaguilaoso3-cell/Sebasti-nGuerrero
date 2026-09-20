

/*
Ejercicio 2: Carrito de Compras con Conteo de Productos
Enunciado: Crear un carrito de compras utilizando LocalStorage, que permita a los
usuarios agregar productos y muestre la cantidad total de productos en el carrito.
1. Los productos deben tener un botón para agregar al carrito.
2. Al agregar un producto, se debe mostrar el número total de productos en el
carrito, almacenándolo en LocalStorage.
3. Al recargar la página, el número total de productos debe recuperarse de
LocalStorage y mostrarse correctamente.
*/


let botones = document.getElementsByClassName("agregar");
let cantidad = document.getElementById("cantidad");


function mostrarCantidad() {

    let cantidadGuardada = localStorage.getItem("cantidad");

    if (cantidadGuardada != null) {
        cantidad.textContent = cantidadGuardada;
    }
}


function agregarProducto() {

    let cantidadActual = localStorage.getItem("cantidad");

    if (cantidadActual == null) {
        cantidadActual = 0;
    }

    cantidadActual++;

    localStorage.setItem("cantidad", cantidadActual);

    cantidad.textContent = cantidadActual;
}


for (let i = 0; i < botones.length; i++) {

    botones[i].addEventListener("click", function() {
        agregarProducto();
    });
}


mostrarCantidad();