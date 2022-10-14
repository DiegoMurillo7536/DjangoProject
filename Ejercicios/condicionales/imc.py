"""
11.Un reporte de salud muestra una tabla diferente del índice de masa corporal IMC de una persona
que se calcula con la fórmula IMC=P/T2 en donde P es el peso en Kg. y T es la talla en metros. Lea un
valor de P y de T, calcule el IMC y muestre su estado según la siguiente tabla:
"""

peso=float(input("Ingrese su peso:"))
talla=float(input("Ingrese su talla en metros:"))
imc=round(peso/talla**2,1)

if imc < 20 :
    print(f"Su imc es de {imc},por lo que está desnutrido")
elif imc > 20 and imc < 25 :
    print(f"Su imc es de {imc},por lo que está normal")
elif imc > 25 and imc < 30 :
    print(f"Su imc es de {imc},por lo que tiene sobrepeso")
elif imc > 30 and imc < 35 :
    print(f"Su imc es de {imc},por lo que tiene obesidad grado 1")
elif imc > 35 and imc < 40 :
    print(f"Su imc es de {imc},por lo que tiene obesidad grado 2")
elif imc > 40 :
    print(f"Su imc es de {imc},por lo que tiene obesidad grado 3")