"""
2. Escriba un programa para encontrar la suma de los primeros 20
 números naturales. El total es 210.
"""

CANTIDAD_NUMEROS=20
numeros=[]
for i in range(CANTIDAD_NUMEROS) :
    numeros.append(i+1)
    print(numeros)

print(sum(numeros))

    
    