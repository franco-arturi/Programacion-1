"""

Crear una función que retorne una lista que tenga los valores pares que se
encuentren dentro de un rango dado (dicho rango se recibe como parámetro
de la función: desde/hasta)

"""


def listaRango(inicio,final):
    lista = []
    for i in range(inicio,final):
        if i % 2 == 0:
            lista.append(i)
    return lista

print(listaRango(20,100))

