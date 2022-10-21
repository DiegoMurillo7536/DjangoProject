"""
9.9. Solicitar un número al usuario, hacer un conteo regresivo en pasos de uno,
partiendo del número ingresado hasta que sea cero 0 y mostrar los números.
"""
numero=int(input("Ingrese un número para el conteo regresivo"))

while numero > 0 :
    print(numero)
    numero=numero-1
