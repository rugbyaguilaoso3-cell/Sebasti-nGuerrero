/*1. Confeccionar una página que muestre dos objetos de la clase RADIO solicitando que
seleccione si es mayor de 18 años o no. Al presionar un botón mostrar un alert
indicando si puede ingresar al sitio o no. */



function mostrarSeleccionado(){

 if (document.getElementById('radio1').checked){
    alert("usted es mayor de 18 años y puede ingresar al sitio")
 }
 
 if(document.getElementById('radio2').checked){
    alert("usted es menor de 18 años y no tiene permitido ingresar al sitio")
 }

 

}