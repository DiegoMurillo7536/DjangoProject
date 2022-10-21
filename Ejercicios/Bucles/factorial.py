"""
9.Escriba un programa para calcular el factorial de un número dado.
"""



import math


FACTORIAL= int(input("Ingrese el numero factorial que desee")) 
numeros = []
for i in range(FACTORIAL):
    numero= i + 1
    numeros.append(numero)
print(math.prod(numeros))