"""
8.Leer el número de llantas de una compra y mostrar el valor que debe pagarse. El almacén las vende
con la siguiente política: Si se compran menos de 5 llantas, el precio unitario es $240000. Si se
compran 6 o 7, el precio unitario es $221000, y si se compran más de 7 llantas, el precio unitario es
$180000.
"""

numero_llantas=int(input("Ingrese el número de llantas que desea:"))

if numero_llantas < 5 : 
    precio_unitario=240000
    total=numero_llantas*precio_unitario
    print(f"Cantidad de llantas {numero_llantas} y precio su precio unitario {precio_unitario}")
    print(f"El valor que se debe pagar es de {total}")


if numero_llantas > 5 and  numero_llantas <= 7  : 
    precio_unitario=221000
    total=numero_llantas*precio_unitario
    print(f"Cantidad de llantas {numero_llantas} y precio su precio unitario {precio_unitario}")
    print(f"El valor que se debe pagar es de {total}")

if numero_llantas > 7 : 
    precio_unitario=180000
    total=numero_llantas*precio_unitario
    print(f"Cantidad de llantas {numero_llantas} y precio su precio unitario {precio_unitario}")
    print(f"El valor que se debe pagar es de {total}")


