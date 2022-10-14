"""
6.Solicitar tres números al usuario e imprimirlos en orden descendente (de mayor a menor).
"""


CANTIDAD_NUMEROS=3
numeros=[]
for i in range(CANTIDAD_NUMEROS) :
    numero= int(input(f"Ingresa el número {i + 1}: "))
    numeros.append(numero)

print(sorted(numeros,reverse=True))
