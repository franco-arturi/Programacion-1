#Generar una lista de 50 numeros aleatorios del 1 al 100. 
# Utilice comprension de listas para generar el resultado

import random as r 
lista=[r.randint(1,100) for i in range(50)]

#Recibir una lista como parametro y devolver True si la misma contiene algun elemento repetido. 
# La funcion no debe modificar la lista.

def elementosRepetidos(lista):
    for i in lista:
        if lista.count(i) > 1:
            return True
    return False    

x=[1,2,3,4]



#Recibir una lista como parámetro y devolver una nueva lista 
#con los elementos únicos de la lista original, sin importar el orden.

def listaNueva(lis):
    aux=list(set(lista))
    return aux

print(listaNueva(lista))