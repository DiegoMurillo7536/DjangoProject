n = int(input("¿Cuántas filas quieres?")) 
x=1 
y=1 
z=1
frase = ''  
for x in range(1,n+1):
    for z in range(1,x+1):
        frase+=(str(y)+(' '))
        y+=1
        print(frase)          
         
    