"""

Crea una función esDivisible que acepte un número como argumento, y una lista de números, 
y devuelva una nueva lista con los números de la lista que son divisibles por el número dado. 
Utiliza funciones lambda y filter para implementarla.

"""

def esDivisible(num,lis):
    return list(filter(lambda y: y%num==0,lis))

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(esDivisible(2,x))

