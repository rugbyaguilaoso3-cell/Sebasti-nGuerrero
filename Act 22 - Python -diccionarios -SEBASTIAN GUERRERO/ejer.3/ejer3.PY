"""
3-

Un equipo de seguridad informática registra las direcciones IP de servidores
sospechosos que intentan acceder de forma no autorizada al sistema.
 Crear un diccionario donde la Clave sea la dirección IP (cadena de
caracteres, ej: &quot;192.168.1.50&quot;) y el Valor sea una tupla que contenga:
(nombre_del_dispositivo, cantidad_intentos_fallidos).
Desarrollar las siguientes funciones:
1. Cargar registro: Solicitar por teclado la carga de 4 direcciones IP
sospechosas junto a los datos del dispositivo y sus intentos fallidos.
2. Listar amenazas: Imprimir la lista de todas las IPs registradas indicando
qué dispositivo es y cuántos intentos realizó.
3. Filtrar Bloqueos: Recorrer el diccionario e informar las direcciones IP que
deben ser bloqueadas inmediatamente por seguridad (aquellas con más de
5 intentos fallidos).
"""

def cargar():
    ips={}
    x=0
    while x<4:
        ip=input("Ingrese la IP: ")
        dispositivo=input("Ingrese el nombre del dispositivo: ")
        intentos=int(input("Ingrese los intentos fallidos: "))
        ips[ip]=(dispositivo,intentos)
        x=x+1
    return ips

def listado(ips):
    print("Listado de amenazas")
    for ip in ips:
        print(ip, ips[ip][0], ips[ip][1])

def bloqueos(ips):
    print("IPs que deben bloquearse")
    for ip in ips:
        if ips[ip][1]>5:
            print(ip)

ips=cargar()
listado(ips)
bloqueos(ips)


