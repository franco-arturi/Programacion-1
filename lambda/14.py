"""

Crea una función masCorto que acepte una lista de strings como argumento y 
devuelva el string más corto de la lista. 
Utiliza la función reduce y una función lambda para implementarla

"""

import functools as f 

def masCorto(lis):
    return f.reduce(lambda x,y: y if len(x)>len(y) else x,lis)

x=(str(input("Texto: "))).split()
print(masCorto(x))