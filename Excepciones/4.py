"""
El método index permite buscar un elemento dentro de una lista, devolviendo 
la posición que éste ocupa. Sin embargo, si el elemento no pertenece a la 
lista se produce una excepción de tipo ValueError. Desarrollar un programa 
que cargue una lista con números enteros ingresados a través del teclado 
(terminando con -1)y permita que el usuario ingrese el valor de algunos elementos 
para visualizar la posición que ocupan, utilizando el método index. Si el número no 
pertenece a la lista se imprimirá un mensaje de error y se solicitará otro para buscar. 
Abortar el proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""


def ingresar():
    x=[]
    y=int(input("Numero: "))
    while y != -1:
        x.append(y)
        y=int(input("Numero: "))
    return x

def buscar(n,lis):
    try:
        return lis.index(n)
    except ValueError:
        print('No existe el indice de esta posicion.')
    
lista=ingresar()
num = int(input("Ingrese numero a buscar su indice: "))
while num != -1:
    print(f'El numero {num} se ecuentra en la posicion {buscar(num,lista)}')
    num = int(input("Ingrese numero a buscar su indice: "))

