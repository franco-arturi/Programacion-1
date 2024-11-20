"""

 Utilizando map, crear un programa que cargue 10 notas de alumnos y, al 
finalizar, genere una nueva lista indicando el estado de aprobación (reutilice 
lo creado en el punto 1).

"""
notas=[6,8,6,8,9,2,3,1,6,4]
aprobado = (lambda nota: True if nota >= 4 else False )
estado=list(map(aprobado,notas))

print(estado)