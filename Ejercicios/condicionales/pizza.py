"""
El precio que debe pagar un cliente por una pizza depende del tamaño seleccionado, como se
muestra a continuación:

9.Si cada ingrediente adicional cuesta $4.000. Escribir un programa que solicite al empleado
encargado de registrar las ventas, el tamaño de la pizza y el número de ingredientes adicionales y
muestre al cliente el precio que debe pagar.
"""
precio_pizza= [15000,24000,36000]
print(f"Tamaño 1:{precio_pizza[0]}")
print(f"Tamaño 2:{precio_pizza[1]}")
print(f"Tamaño 3:{precio_pizza[2]}")
opcion=int(input("Ingrese el tamaño que desea:1,2 o 3:"))

if opcion == 1 :
    print("¿Desea ingredientes adicionales?")
    cantidad=int(input("Si es el caso ingrese la cantidad, de lo contrario ponga 0:"))
    total= precio_pizza[0]+(cantidad*4000)
    print(f"El total de la pizza es:{total}")
if opcion == 2 :
    print("¿Desea ingredientes adicionales?")
    cantidad=int(input("Si es el caso ingrese la cantidad, de lo contrario ponga 0:"))
    total= precio_pizza[1]+(cantidad*4000)
    print(f"El total de la pizza es:{total}")
if opcion == 3 :
    print("¿Desea ingredientes adicionales?")
    cantidad=int(input("Si es el caso ingrese la cantidad, de lo contrario ponga 0:"))
    total= precio_pizza[2]+(cantidad*4000)
    print(f"El total de la pizza es:{total}")