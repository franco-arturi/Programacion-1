""""

Crear un programa que intercambie el primer y último elemento de una lista
precargada

"""

lista=[1,2,3,4,5,6,7,8,9]
def cambiarOrden(lista):
    aux=lista[0]
    lista[0]=lista[-1]
    lista[-1]=aux

