"""

 Modifique la función anterior, haciendo uso de filter, para poder obtener una 
lista de notas aprobadas y otro de desaprobadas.

"""
notas=[6,8,6,8,9,2,3,1,6,4]
aprobado = (lambda nota:  nota >= 4 )
estado=list(filter(aprobado,notas))

print(estado)