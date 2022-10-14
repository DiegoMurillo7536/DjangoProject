"""
2.Solicitar número al usuario y determinar si es negativo, positivo o cero.
"""
numero=int(input("Ingrese un numero para saber si es positivo o negativo:"))

if numero == 0 :
    print("El número es:",numero)
if numero > 0 :
    print("Es un número positivo")
if numero < 0:
    print("Es un número negativo")
