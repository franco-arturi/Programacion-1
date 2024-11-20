"""

Desarrollar cada una de las siguientes funciones y escribir un programa
que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:

a. Cargar una lista con números al azar de cuatro dígitos. La 
cantidad de elementos también será un número al azar de dos dígitos. 
Realice la composición de la lista por comprensión y de la forma habitual 
(tendrá dos funciones distintas).

b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.

c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a 
eliminar se ingresa desde el teclado y la función lo recibe como parámetro. 
Utilice comprensión de listas para resolverlo.

d. Determinar si el contenido de una lista cualquiera es capicúa, sin
usar listas auxiliares. Un ejemplo de lista capicúa es [50,17,91,17,50].

"""

import random as r


#A
def cargarLista():
    lista=[]
    for i in range(r.randint(10,99)):
        lista.append(r.randint(1000,9999))
    return lista

def cargarListaComprension():
    lista={r.randint(1000,9999) for x in range(r.randint(10,99))}
    return lista

#B

def suma(lista):
    return (sum(lista))

def eliminarNum(lista):
    








