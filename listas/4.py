""""

Modifique el ejercicio anterior para que, en caso de que una de las listas
tenga más elementos que la otra, se sumen dichos elementos al final de la
nueva lista

"""

def cambiarOrden(lista1, lista2):
    listaAux=[]
    if len(lista1)!=len(lista2):
        if len(lista1)>len(lista2):
            for i in range(len(lista2)):
                listaAux.append(lista1[i])
                listaAux.append(lista2[i])
            for i in range(len(lista2),len(lista1)):
                listaAux.append(lista1[i])
            return listaAux
        elif len(lista2)>len(lista1):
            for i in range(len(lista1)):
                listaAux.append(lista1[i])
                listaAux.append(lista2[i])
            for i in range(len(lista1),len(lista2)):
                listaAux.append(lista2[i])
            return listaAux

    else:

        for i in range(len(lista1)):
            listaAux.append(lista1[i])
            listaAux.append(lista2[i])
        return listaAux


Lista1 = ["Hola","nombre","juan","Carlos","De","Cordoba"]
Lista2 = ["mi","es","Perez"]

print(cambiarOrden(Lista2,Lista1))