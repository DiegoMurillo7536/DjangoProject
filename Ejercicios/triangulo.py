
print("Bienvenido, por favor elige que deseas realizar:")
print("Escribre la abreviación de lo que quieres descubrir")
abreviacion=input("CO: CATETO OPUESTO, CA: CATETO ADYACENTE, H: HIPOTENUSA:")
if(abreviacion=="CO"):
    h=float(input("ingrese la hipotenusa:"))
    ca=float(input("ingrese el cateto adyacente:"))
    if(h<ca):
        print("Lo sentimos, la hipotenusa siempre tiene que tener mayor valor que el CO o el CA")
    else:
        co=(((h**2)-(ca**2))**0.5)
        print("El cateto opuesto es:")
        print(co)
if(abreviacion=="CA"):
    h=float(input("ingrese la hipotenusa:"))
    co=float(input("ingrese el cateto opuesto:"))
    if(h<co):
        print("Lo sentimos, la hipotenusa siempre tiene que tener mayor valor que el CO o el CA")
    else:
        ca=(((h**2)-(co**2))**0.5)
        print("El cateto opuesto es:")
        print(ca)

if(abreviacion=="H"):
    co=float(input("ingrese el cateto opuesto:"))
    ca=float(input("ingrese el cateto adyacente:"))
    h=(((ca**2)+(co**2))**0.5)
    print("La hipotenusa es:")
    print(h)

