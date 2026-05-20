#2. En un banco se procesan datos de las cuentas corrientes de sus clientes. De cada
#cuenta corriente se conoce: número de cuenta y saldo actual. El ingreso de datos debe
#finalizar al ingresar un valor negativo en el número de cuenta. Se pide confeccionar un
#programa que lea los datos de las cuentas corrientes e informe:
#● a) De cada cuenta: número de cuenta y estado de la cuenta según su saldo,
#sabiendo que:
#○ Estado de la cuenta:
#○ “Acreedor” si el saldo es &gt; 0.
#○ “Deudor” si el saldo es &lt; 0.
#○ “Nulo” si el saldo es = 0.
#● b) La suma total de los saldos acreedores.

suma_acreedores = 0

numero_cuenta = int(input("Ingrese número de cuenta: "))

while numero_cuenta >= 0:

    saldo = float(input("Ingrese saldo actual: $"))

    if saldo > 0:
        estado = "Acreedor"
        suma_acreedores = suma_acreedores + saldo

    else:
        if saldo < 0:
            estado = "Deudor"
        else:
            estado = "Nulo"

    print("Cuenta:", numero_cuenta)
    print("Estado:", estado)

    numero_cuenta = int(input("Ingrese número de cuenta: "))

print("Suma total de saldos acreedores:", suma_acreedores)

