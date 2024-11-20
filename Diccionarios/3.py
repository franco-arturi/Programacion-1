"""
 Hacer un programa que registre 10 alumnos y guarde: nombre, nombre de la asignatura 
y 4 notas. Calcular y mostrar el promedio de las notas.
"""
import random as r
def crearalumno():
    x={}
    x["alumno"]=r.randint(0000,9999)
    x["asignatura"]=r.choice(["a","b","c"])
    x["nota1"]=r.randint(1,10)
    x["nota2"]=r.randint(1,10)
    x["nota3"]=r.randint(1,10)
    x["nota4"]=r.randint(1,10)
    return x

def main():
    alumnos=[]
    for i in range(10):
        alumnos.append(crearalumno())
    for i in alumnos:
        promedio=(i["nota1"]+i["nota2"]+i["nota3"]+i["nota4"])//4
        alu=i["alumno"]
        print(f"{alu}  {promedio}")

main()

