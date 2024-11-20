"""

Crear una función que elimine los elementos de una lista que tenga
determinado valor

"""

def eliminarElemento(elemento,lista):
    while elemento in lista:
        lista.remove(elemento)
    return

lista=[1,2,3,4,5,6,7,7,7,8,9]
eliminarElemento(7,lista)
print(lista)
