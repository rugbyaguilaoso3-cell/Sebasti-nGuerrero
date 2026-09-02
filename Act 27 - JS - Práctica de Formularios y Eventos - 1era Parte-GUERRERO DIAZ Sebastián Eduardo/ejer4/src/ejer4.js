/* 4. Confeccionar una página que muestre un objeto SELECT con distintos
tipos de pizzas (Jamón y Queso, Muzzarella, Morrones). Al seleccionar
una, mostrar en un objeto de tipo TEXT el precio de la misma.*/



let pizza = document.getElementById("pizza");
let precio = document.getElementById("precio");

pizza.addEventListener("change", function() {

    precio.value = pizza.value;

});