""" 
Desarrolle un programa que procese una tabla con 10 horarios (hora -de 0 a 23- y
minutos) en formato tupla; e indique por cada una de ellas: si es AM o PM y cuántos
minutos falta para la próxima hora  
El resultado de AM/PM y la cantidad de minutos se debe almacenar en una lista de
tuplas con los valores originales y los resultados. Imprimir el resultado final en
pantalla.

"""

horarios = [(8, 30),(12, 45),(15, 0),(18, 20),(9, 50),(14, 15),(19, 35),(22, 10),(6, 5),(23, 59)]
tupla=()

for i in horarios:
    if i[0] < 12:

        tupla=tupla+((i, "AM", 60 - i[1]),)

    else:

        i=i+((i, "PM", 60 - i[1]),)
        tupla=tupla+((i,"PM", 60 - i[1]),)

print(tupla)

horas = [(8, 30), (12, 45), (15, 0), (18, 20), (9, 50), (14, 15), (19, 35), (22, 10), (6, 5), (23, 59)]
tupla = ()

for i in horas:
    if i[0] < 12:

        tupla=tupla+((i, "AM", 60 - i[1]),)
    else:
        tupla=tupla+((i, "PM", 60 - i[1]),)

print(tupla)