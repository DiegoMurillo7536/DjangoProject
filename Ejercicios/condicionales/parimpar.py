"""
1.Par o impar. Solicitar número al usuario y determinar si es par, impar o es cero
"""
numero=  int(input("Ingrese un número para saber si es par o impar:"))

if numero != 0: 
    print ("El número es diferente de cero")
else:
    print("El número es cero")
if numero % 2 == 0 :
    print("El número es par")
if numero % 3 == 0 :
    print ("El número es impar")
