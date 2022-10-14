"""
7.Programa que permita a un usuario tomar una decisión del tipo de pago a usar. Si la cuenta es menor
a $150000 pago en efectivo. Si no, si es de $150000 hasta $300000 pago con el celular (dinero
electrónico). Si es mayor a $300000 hasta $600000, pago con la tarjeta de débito. Caso contrario,
pago con la tarjeta de crédito.
"""

tipopago=  ["Pago en efectivo","Pago con el celular","Tarjeta débito","Tarjeta crédito"]
cuenta=  int(input("Ingrese el monto de dinero que va a pagar:"))

if cuenta >= 600000 :
    print(f" Usted tiene las siguientes maneras de pagar: {tipopago[0]},{tipopago[1]},{tipopago[2]} y {tipopago[3]}")

if cuenta < 600000 and cuenta > 300000 :
    print(f" Usted tiene las siguientes maneras de pagar: {tipopago[0]},{tipopago[1]} y {tipopago[2]}")

if cuenta > 150000 and cuenta < 300000 :
     print(f" Usted tiene las siguientes maneras de pagar: {tipopago[0]} y {tipopago[1]}")

if cuenta < 15000 :
    print(f" Usted tiene la siguiente manera de pagar: {tipopago[0]}")
