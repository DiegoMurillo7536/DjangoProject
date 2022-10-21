"""
7. Conversión de temperaturas. Crear un menú de opciones. 
"""
"""
Fahrenheit-Celsius C = ( F - 32) / 1.8
Fahrenheit-kelvin K = ( F + 459.67) / 1.8
Fahrenheit-Rankine Ra = F + 459.67
Fahrenheit-Réaumur Re = ( F - 32) / 2.25
"""
print("1.Fahrenheit-Celsius C = ( F - 32) / 1.8")
print("2.Fahrenheit-kelvin K = ( F + 459.67) / 1.8")
print("3.Fahrenheit-Rankine Ra = F + 459.67")
print("4.Fahrenheit-Reaumur Re = ( F - 32) / 2.25")
print("5.Celsius-Fahrenheit F = C × 1.8 + 32")
print("6.Celsius-kelvin K = C + 273.15")
print("7.Celsius-Rankine Ra = C × 1.8 + 32 + 459.67")
print("8.Celsius-Reaumur Re = C × 0.8")
print("9.kelvin-Celsius C = K - 273.15")
print("10.kelvin-Fahrenheit F = K × 1.8 - 459.67")
print("11.kelvin-Rankine Ra = K × 1.8")
print("12.kelvin-Réaumur Re = (K - 273.15) × 0.8")
print("13.Rankine-Celsius C = ( Ra - 32 - 459.67) / 1.8")
print("14.Rankine-Fahrenheit F = Ra - 459.67")
print("15.Rankine-kelvin K = Ra / 1.8 ")
print("16.Rankine-Réaumur Re = ( Ra - 32 - 459.67) / 2.25")
print("17.Réaumur-Celsius C = Re × 1.25")
print("18.Réaumur-Fahrenheit F = Re × 2.25 + 32")
print("19.Réaumur-Kelvin K = Re × 1.25 + 273.15")
print("20.Réaumur-Rankine Ra = Re × 2.25 + 32 + 459.67")

opcion=int(input("Ingrese el numero del menu para la conversión"))

if opcion == 5 :
    C = int(input("Ingrese los grados:"))
    F = C * 1.8 + 32
    print(F)

elif opcion == 17 :
    Re = int(input("Ingrese los grados:"))
    C = Re * 1.25
    print(C)

elif opcion == 18 :
    Re = int(input("Ingrese los grados:"))
    F = Re * 2.25 + 32
    print(F)

elif opcion == 19 :
    Re = int(input("Ingrese los grados:"))
    K = Re * 1.25 + 273.15
    print(K)

elif opcion == 20 :
    Re = int(input("Ingrese los grados:"))
    Ra = Re * 2.25 + 32 + 459.67
    print(Ra)

elif opcion == 13 :
    Ra = int(input("Ingrese los grados:"))
    C = ( Ra - 32 - 459.67) / 1.8
    print(C)

elif opcion == 14 :
    Ra = int(input("Ingrese los grados:"))
    F = Ra - 459.67
    print(F)

elif opcion == 15 :
    Ra = int(input("Ingrese los grados:"))
    K = Ra / 1.8
    print(K)

elif opcion == 16 :
    Ra = int(input("Ingrese los grados:"))
    Re = ( Ra - 32 - 459.67) / 2.25
    print(Re)


elif opcion == 9 :
    K = int(input("Ingrese los grados:"))
    C = K - 273.15
    print(C)

elif opcion == 10 :
    K = int(input("Ingrese los grados:"))
    F = K * 1.8 - 459.67
    print(F)

elif opcion == 11 :
    K = int(input("Ingrese los grados:"))
    Ra = K * 1.8
    print(Ra)

elif opcion == 12 :
    K = int(input("Ingrese los grados:"))
    Re = (K - 273.15) * 0.8
    print(Re)


elif opcion == 6 :
    C = int(input("Ingrese los grados:"))
    K = C + 273.15
    print(K)

elif opcion == 7 :
    C = int(input("Ingrese los grados:"))
    Ra = C * 1.8 + 32 + 459.67
    print(Ra)

elif opcion == 8 :
    C = int(input("Ingrese los grados:"))
    Re = C * 0.8
    print(Re)

elif opcion == 1  :
    F = int(input("Ingrese los grados:"))
    C= (F-32)/1.8
    print(C)
elif opcion == 2  :
    F = int(input("Ingrese los grados:"))
    K = ( F + 459.67) / 1.8
    print(K)
elif opcion == 3  :
    F = int(input("Ingrese los grados:"))
    Ra = F + 459.67
    print(Ra)
elif opcion == 4  :
    F = int(input("Ingrese los grados:"))
    Re = ( F - 32) / 2.25
    print(Re)

