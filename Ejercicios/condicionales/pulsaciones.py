"""
12.El número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico
se calcula con la fórmula:
Género femenino (1): número de pulsaciones = (220 - edad en años)/10
Género masculino (2): número de pulsaciones = (210 - edad en años)/10
Lea la edad y el género y muestre el número de pulsaciones.
"""

genero=  input("Ingrese la letra de su genero,Masculino(M),Femenino(F):")
edad=  int(input("Ingrese su edad:"))

if genero == "M" or "m" :
    pulsaciones=(210-edad)/10
    print(f"Cantidad de pulsaciones por segundo:{pulsaciones}")
if genero == "F" or "f" :
    pulsaciones=(220-edad)/10
    print(f"Cantidad de pulsaciones por segundo:{pulsaciones}")