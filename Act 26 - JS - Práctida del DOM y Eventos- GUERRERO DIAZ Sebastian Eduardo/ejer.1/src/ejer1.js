/*
JavaScript – DOM y Eventos - Ejercicios.

Ejercicio 01: Modificación del DOM con Métodos de Selección
Enunciado: Crear un programa que, al hacer clic en un botón, cambie el contenido de
un párrafo en la página utilizando los métodos para acceder al DOM. Los pasos
específicos son:
1. Al cargar la página, se debe mostrar un párrafo con el texto: &quot;Texto inicial&quot;.
2. Al hacer clic en un botón, se debe cambiar ese texto por: &quot;El texto ha sido
modificado con JavaScript&quot;.
3. Usar getElementById() para seleccionar el párrafo y modificar su contenido con
textContent. 
 */



let texto = document.getElementById("texto");
let boton = document.getElementById("boton");

boton.addEventListener("click", function() {
    texto.textContent = "El texto ha sido modificado con JavaScript";
});
