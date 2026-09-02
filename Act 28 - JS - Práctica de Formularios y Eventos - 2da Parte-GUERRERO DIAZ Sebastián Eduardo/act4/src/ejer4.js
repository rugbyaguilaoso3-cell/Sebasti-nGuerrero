/* 4. Modificar el segundo problema resuelto de los ejemplos de la sección “Eventos
onMouseOver y onMouseOut.” Del material 11. (las casillas de la tabla que cambian el
color cuando ingresamos con el mouse) para permitir llamar mediante hipervínculos a
distintos programas que administran web-mail (Gmail, Hotmail y Yahoo!) */



let gmail = document.getElementById("gmail");
let hotmail = document.getElementById("hotmail");
let yahoo = document.getElementById("yahoo");

gmail.addEventListener("mouseover", function() {
    window.location.href = "https://mail.google.com";
});

hotmail.addEventListener("mouseover", function() {
    window.location.href = "https://outlook.live.com";
});

yahoo.addEventListener("mouseover", function() {
    window.location.href = "https://mail.yahoo.com";
});