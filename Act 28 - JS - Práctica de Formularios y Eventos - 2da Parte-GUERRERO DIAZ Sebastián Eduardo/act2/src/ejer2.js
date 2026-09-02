/*2. Confeccionar una página de visitas a un sitio, solicitar ingresar el nombre de una
persona, su mail y los comentarios (TEXTAREA). Mostrar luego llamando a la función
alert los datos ingresados. */


let boton = document.getElementById('boton');
let nom = document.getElementById('nom');
let mail = document.getElementById('mail');
let comentarios = document.getElementById('comentarios');
boton.addEventListener("click",function(){
    alert("  nombre: " + nom.value + "  mail: "+ mail.value + "  comentarios: " + comentarios.value)
});




