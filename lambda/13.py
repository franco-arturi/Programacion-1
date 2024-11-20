"""

 Crea una función productoPares que acepte una lista de números como argumento y devuelva el 
 producto de todos los números pares de la lista. Utiliza la función reduce y 
 una función lambda para implementarla.

"""
import functools as f

def productoPares(lis):
    return f.reduce(lambda x,y: x*y if y%2==0 else x,lis)
x=[3,2,3,4,5,6,7,8,9,9,10]
print(productoPares(x))