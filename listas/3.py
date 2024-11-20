"""

Crear un programa que combine dos listas en un recorrido sucesivo de sus
índices en una tercera. Si las listas tienen diferentes longitudes, se debe
notificar en pantalla que el proceso no se puede realizar. Ejemplo:
Lista1 = [“Hola”,”nombre”,”juan”]
Lista2 = [“mi”,”es”,”Perez”]

"""

def cambiarOrden(lista1, lista2):
    if len(lista1)!=len(lista2):
        return -1
    else:
        listaAux=[]
        for i in range(len(lista1)):
            listaAux.append(lista1[i])
            listaAux.append(lista2[i])
        return listaAux


Lista1 = ["Hola","nombre","juan"]
Lista2 = ["mi","es","Perez"]

print(cambiarOrden(Lista1,Lista2))


