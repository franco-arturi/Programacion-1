

"""

Eliminar de una lista de palabras las palabras que se encuentren en una segunda lista. 
Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

"""

x=["as","aass","htdc","a","as","ssda3","as"]
z=["as","a"]

def eliminarPalabras(l1,l2):
    print(l1)
    print(l2)
    for i in l2:
        while i in l1:
            l1.remove(i)
    print(l1)

eliminarPalabras(x,z)