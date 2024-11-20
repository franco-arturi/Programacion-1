"""

Crea una función dobleSiEsPar que acepte una lista de números como argumento, 
devuelva una nueva lista con cada número multiplicado por dos si es par, y elimine 
todos los números impares de la lista. Utiliza funciones lambda, map y filter para implementarla.

"""

def dobleSiEsPar(lis):
    aux=list(map(lambda x: x*2 if x % 2 == 0 else x,lis))
    return list(filter(lambda x: x%2==0,aux))

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(dobleSiEsPar(x))