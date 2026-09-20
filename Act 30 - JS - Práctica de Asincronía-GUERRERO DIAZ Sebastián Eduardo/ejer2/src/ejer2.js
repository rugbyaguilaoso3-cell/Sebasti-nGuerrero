

/*

*/


let productos = document.getElementById("productos");
let cantidad = document.getElementById("cantidad");
let listaCarrito = document.getElementById("lista-carrito");


function obtenerProductos() {

    fetch("https://fakestoreapi.com/products")
        .then(function(respuesta) {
            return respuesta.json();
        })
        .then(function(datos) {
            mostrarProductos(datos);
        })
        .catch(function() {
            productos.textContent = "Ocurrió un error al cargar los productos.";
        });
}


function mostrarProductos(datos) {

    for (let i = 0; i < datos.length; i++) {

        let producto = document.createElement("div");
        producto.className = "producto";

        let imagen = document.createElement("img");
        imagen.src = datos[i].image;

        let nombre = document.createElement("h2");
        nombre.textContent = datos[i].title;

        let precio = document.createElement("p");
        precio.textContent = "$" + datos[i].price;

        let boton = document.createElement("button");
        boton.textContent = "Añadir al carrito";

        boton.addEventListener("click", function() {
            agregarProducto(datos[i]);
        });

        producto.appendChild(imagen);
        producto.appendChild(nombre);
        producto.appendChild(precio);
        producto.appendChild(boton);

        productos.appendChild(producto);
    }
}


function agregarProducto(producto) {

    let carrito = JSON.parse(localStorage.getItem("carrito")) || [];

    carrito.push(producto);

    localStorage.setItem("carrito", JSON.stringify(carrito));

    mostrarCarrito();
}


function mostrarCarrito() {

    let carrito = JSON.parse(localStorage.getItem("carrito")) || [];

    listaCarrito.innerHTML = "";

    for (let i = 0; i < carrito.length; i++) {

        let li = document.createElement("li");

        li.textContent = carrito[i].title + " - $" + carrito[i].price;

        listaCarrito.appendChild(li);
    }

    cantidad.textContent = carrito.length;
}


obtenerProductos();
mostrarCarrito();