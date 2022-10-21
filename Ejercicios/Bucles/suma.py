"""
Escribe un programa para leer 10 
números del teclado y encontrar su suma y promedio.
"""
CANTIDAD= 10
numeros = []
for i in range(CANTIDAD):
    numero= int(input(f"Ingresa el número {i + 1}: "))
    print(numero)
    numeros.append(numero)
    suma=sum(numeros)
    prom=(sum(numeros)/CANTIDAD)      
print(f"La suma de los numeros es: {suma} y el promedio es: {prom}")
