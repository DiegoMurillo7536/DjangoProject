"""
3.Solicitar dos números al usuario y calcular cuál es el mayor y cuál el menor, e imprimir los resultados
"""

a=int(input("Ingrese el primer número:"))
b=int(input("Ingrese el segundo número:"))

if a > b :
    print("El número mayor es",a)

if b > a :
    print("El número mayor es",b)

if a == b :
    print("Ambos números son iguales")

