"""
5. Escriba un programa para 
mostrar la tabla de multiplicar de un entero dado.
"""
contador=0
numero=int(input("Ingrese un número para multiplicar:"))
while contador <= 10 :
    multiplicacion=numero*contador
    contador=contador+1
    print(multiplicacion)