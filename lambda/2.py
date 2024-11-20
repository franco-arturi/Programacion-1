"""

Escriba un programa para generar una función (utilizando filter) y lambdas
para separar los números pares e impares de una lista de números. La 
función debe retornar dos valores resultantes.

"""
lista=[1,2,3,4,5,6,7,8,9]
lista1=list(filter(lambda x:x%2==0,lista))
lista2=list(filter(lambda x:x%2!=0,lista))
print(lista1,lista2)