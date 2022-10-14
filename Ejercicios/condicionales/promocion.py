"""
10.Un local vende sus productos con la siguiente promoción. Si compra hasta 5 artículos, no hay
descuento. Si compra más de 5 artículos, pero menos de 10, el precio unitario se reduce en 5%. Si
compra 10 o más artículos, el precio unitario se reduce en 8%. Ingrese un dato de cantidad y el valor
del precio unitario original. Calcule y muestre el valor total a pagar.
"""

cantidad=  int(input("Ingrese la cantidad de articulos que desea:"))
valor_unitario= int(input("Ingrese el valor unitario de los articulos:"))

if cantidad >= 10 :
    descuento=0.8
    total=cantidad*(valor_unitario*descuento)
    print(f"el valor total de la compra es de:{total}, su descuento fue del 8%")

if cantidad > 5 and cantidad < 10 :
    descuento=0.5
    total=cantidad*(valor_unitario*descuento)
    print(f"el valor total de la compra es de:{total}, su descuento fue del 5%")

if cantidad < 5 :
    total=cantidad*(valor_unitario)
    print(f"el valor total de la compra es de:{total}, esta vez usted no tuvo descuento")