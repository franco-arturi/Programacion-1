""" 
  Cálculo de promedio: crea un programa que lea una lista de tuplas, donde cada tupla
contiene el nombre de un estudiante y una lista de calificaciones, y calcule el
promedio de calificaciones de cada estudiante.
Por ejemplo, si llamamos a la función con la lista de tuplas [( 'Juan', [9, 8, 7]),
('Maria', [10, 9, 10]), ('Pedro', [8, 7, 9])], la función devolverá la lista [( 'Juan', 8.0),
('Maria', 9.67), ('Pedro', 8.0)], que contiene el nombre de cada estudiante y su
promedio de calificaciones en forma de tuplas  
"""
estudiantes=[( 'Juan', [9, 8, 7]),('Maria', [10, 9, 10]), ('Pedro', [8, 7, 9])]
def promedio(lista):
    aux=[]
    for i in lista:
        promedio=(i[1][0]+i[1][1]+i[1][2])/3
        auxIn=[i[0],promedio]
        aux.append(tuple(auxIn))
    return aux
print(promedio(estudiantes))