lineas=int(input("Ingrese la cantidad de lineas"))
numero=int(input("Ingrese el numero que desea imprimir"))
for i in range(lineas):
		x = lineas - i - 1
		z = i * 2 + 1
		print (" " * x + str(numero) * z)