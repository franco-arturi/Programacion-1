"""

Crea una función filtraMayores que acepte una lista de números como argumento y 
devuelva una nueva lista con los números mayores que 5. Utiliza la función 
filter para implementarla.

"""

def filtraMayores(lis):
    return list(filter(lambda x: x>5,lis))

x=[1,2,3,4,5,6,7,8,9,11,23,45,12]
print(filtraMayores(x))

