"""
Sistema de calificaciones: 
Escribe un programa que permita a los profesores registrar las calificaciones de sus alumnos y les permita calcular la nota final. 
Crea un diccionario para cada alumno, con su legajo como clave y una lista de notas como valor.
Luego, el programa debe permitir al usuario ingresar las notas para cada alumno y calcular su nota final, basándose en un sistema de pasos predeterminado.
"""
alumnos={123:[5,4,8],321:[2,7,6]}
def cargarAlumnos():
    alumno={}
    legajo=int(input("Ingrese legajo del alumno: "))
    nota1=int(input("Ingrese nota del alumno: "))
    nota2=int(input("Ingrese nota del alumno: "))
    alumno[legajo]=[nota1,nota2,(nota1+nota2)//2]
    return alumno

def main():
    op=0
    while op!=3:
        opInter=int(input("Ingrese operacio, 1 cargar alumno, 2 ver alumnos o 3 salir"))
        if opInter == 1:
            alumnos.update(cargarAlumnos())
        elif opInter == 2:
            print(alumnos)
        elif opInter == 3:
            op = 3

main()