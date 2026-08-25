/* 
Ejercicio 05: Control de Temperatura
Diseñar una página con un campo de texto para ingresar una temperatura y un botón
“Verificar”.
Cuando el usuario haga clic:
 Si la temperatura es menor a 10, mostrar en el documento el mensaje “Hace
frío” en azul.
 Si está entre 10 y 25, mostrar “Clima agradable” en verde.
 Si es mayor a 25, mostrar “Hace calor” en rojo.
Además, cada verificación debe registrarse en consola con la fecha y hora
exacta (usando Date()).
*/

let temperatura = document.getElementById("temperatura");
let boton = document.getElementById("verificar");
let resultado = document.getElementById("resultado");
boton.addEventListener("click", function() {

    let valor = parseFloat(temperatura.value);

    if (valor < 10) {

        resultado.textContent = "Hace frío";
        resultado.style.color = "blue";

    }
    else if (valor <= 25) {

        resultado.textContent = "Clima agradable";
        resultado.style.color = "green";

    }
    else {

        resultado.textContent = "Hace calor";
        resultado.style.color = "red";

    }

    console.log("Verificación realizada:", new Date());
});
