"""
6. Escriba un programa para mostrar el patrón como triángulo con un asterisco. El patrón como:
    
    ```
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
"""
asteriscos= ["*","**","***","****","*****",]
contador=0
while contador<= 4 :
    print(asteriscos[contador])
    contador=contador+1
while contador>= 1 :
    print(asteriscos[contador-1])
    contador=contador-1

    