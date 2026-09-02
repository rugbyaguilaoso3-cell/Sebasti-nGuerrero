/*3. Disponer dos campos de texto tipo password. Cuando se presione un
botón mostrar si las dos claves ingresadas son iguales o no (es muy
común solicitar al operador el ingreso de dos veces de su clave para
validar si las escribió correctamente, esto se hace cuando se crea una
password para el ingreso a un sitio o para el cambio de una existente).
Tener en cuenta que podemos emplear el operador == para ver si dos
string son iguales.*/


let clave1 = document.getElementById("clave1");
let clave2 = document.getElementById("clave2");

let boton = document.getElementById("boton");
let resultado = document.getElementById("resultado");

boton.addEventListener("click", function() {

    if (clave1.value == clave2.value) {
        resultado.textContent = "Las claves son iguales";
    }
    else {
        resultado.textContent = "Las claves no son iguales";
    }

});