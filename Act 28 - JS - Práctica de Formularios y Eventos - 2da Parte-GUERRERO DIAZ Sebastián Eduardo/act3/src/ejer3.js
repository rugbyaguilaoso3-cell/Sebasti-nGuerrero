/*3. Solicitar que se ingrese el nombre y la clave de un usuario. Mostrar una ventana de
alerta si en la clave se ingresan menos de 7 caracteres o más de 20 (capturar el evento
onBlur) */


function prueba() {
    
    let inputClave = document.getElementById('clave'); 
    let contra = inputClave.value.length; 
    
   
    if (contra < 7 || contra > 20) { 
        alert("ERROR: la clave debe de tener entre 7 y 20 caracteres.");
    }
}

