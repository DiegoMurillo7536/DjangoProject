"""
5.Crear un programa con un menú de opciones, que permita calcular las áreas de figuras geométricas:
cuadrado, rectángulo, triángulo, círculo, rombo y trapecio.
"""
import math


print("Figuras:cuadrado, rectángulo, triángulo, círculo, rombo y trapecio.")
figura=input("Bienvenido, escribe el nombre de la figura que deseas descubrir su area:")

if figura == "cuadrado" :
    lado=int(input("indique cuanto mide el lado del cuadrado:"))
    print("El area del cuadrado es:",lado*lado)
elif figura == "rectangulo" :
    altura=int(input("Ingrese lo largo del rectangulo:"))
    base=int(input("Ingrese lo ancho del rectangulo:"))
    print("El area del rectángulo es:",base*altura)
elif figura == "triangulo" :
    base=int(input("Ingrese lo ancho del triangulo:"))
    altura=int(input("Ingrese lo largo del triangulo:"))
    print("El area del rectángulo es:",((base*altura)/2))
elif figura == "circulo" :
    pi=math.pi
    radio=int(input("Ingrese el radio del circulo:"))
    print("El area del círculo es:",(pi*(radio**2)))

elif figura == "rombo" :
    diagonal_mayor=int(input("Ingrese la diagonal mayor:"))
    diagonal_menor=int(input("Ingrese la diagonal menor:"))

    print("El area del rombo es:",((diagonal_mayor*diagonal_menor)/2))
elif figura == "trapecio" :
    base_mayor=int(input("Ingrese la base mayor:"))
    base_menor=int(input("Ingrese la base menor:"))
    altura=int(input("Ingrese la altura:"))
    area=((base_mayor+base_menor)/2)*altura
    print("El area del trapecio es:",area)
