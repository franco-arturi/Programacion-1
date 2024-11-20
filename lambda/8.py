"""

Crea una función doble que acepte una lista de números como argumento y devuelva
una nueva lista con cada número multiplicado por dos. Utiliza la función map para implementarla.

"""

def multiplicador(num):
    return list(map(lambda x: x*2, num))
x=[1,2,3,4,5,6,7,8,9,0]
print(multiplicador(x))