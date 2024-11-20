"""

Una clínica necesita un programa para atender a sus pacientes. Cada paciente que ingresa se anuncia 
en la recepción indicando su número de afiliado (número entero de 4 dígitos) y además indica si viene por una urgencia 
(ingresando un 0) o con turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego se solicita:


a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de los pacientes atendidos por turno en el orden que llegaron a la clínica.

b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue atendido por turno y cuántas por urgencia.


Repetir esta búsqueda hasta que se ingrese -1 como número de afiliado

"""

numSocio=0
matrizPacientes=[]
numAfiliado=0

while numSocio != -1:
    paciente=[]
    numSocio=int(input("Ingrese numero de socio: "))
    if numSocio != -1:
        estado=int(input("Ingrese urgencia(0) o turno(1): "))
        paciente.append(numSocio)
        paciente.append(estado)
        matrizPacientes.append(paciente)

urgencia=[i[0] for i in matrizPacientes if i[1] == 0]
turno = [i[0] for i in matrizPacientes if i[1] == 1]
print("Pacientes de urgencias: ")
for i in range(len(urgencia)):
    print(f"    Numero Afiliado: {urgencia[i]}")
print("Pacientes por Turno: ")
for i in range(len(turno)):
    print(f"    Numero Afiliado: {turno[i]}")


while numAfiliado != -1:
    numAfiliado=int(input("Ingrese numero afiliado a buscar: "))
    if numAfiliado != -1:
        print(f"Numero de Afiliado: {numAfiliado}")
        print(f"    Este paciente ingreso por urgencia {urgencia.count(numAfiliado)} veces.")
        print(f"    Este paciente ingreso por turno {turno.count(numAfiliado)} veces.")