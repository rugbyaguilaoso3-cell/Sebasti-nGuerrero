/*Ejercicio 4: Algoritmo de Compresión de Texto (RLE)
Contexto: En telecomunicaciones se utiliza el algoritmo Run-Length Encoding (RLE) para
comprimir secuencias de caracteres repetidos y ahorrar ancho de banda.
Consigna: Escribir la función comprimir_rle(texto) que reciba una cadena de caracteres en
mayúsculas y devuelva su versión comprimida.
Requisitos:
● Contar las apariciones consecutivas de cada carácter.
● Construir una cadena resultante intercalando el carácter con su cantidad de
apariciones consecutivas.
Ejemplo de Entrada: &quot;AAABBCDDDD&quot; Salida Esperada: &quot;A3B2C1D4&quot; */
function ingresar(){
    let cadena = prompt("Ingrese el texto:");
    return cadena
}

function comprimirRle(cadena){

    let salida = "";
    let cantidad = 1;

    for(let posicion=0; posicion<cadena.length-1; posicion++){

        if(cadena[posicion] == cadena[posicion+1]){
            cantidad = cantidad + 1;
        }else{
            salida = salida + cadena[posicion] + cantidad;
            cantidad = 1;
        }
    }

    salida = salida + cadena[cadena.length-1] + cantidad;

    return salida;
}

let cadena=ingresar()
let salida = comprimirRle(cadena);

console.log("Texto comprimido:", salida);


