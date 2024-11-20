"""

Escriba un programa Python para encontrar números divisibles por 3 de una 
lista de números usando Lambda.

"""
lista=[1,2,3,4,5,6,7,8,9]
divisibleTres=(lambda x: True if x%3==0 else False)
for i in lista:
    if divisibleTres(i)==True:
        print(i)