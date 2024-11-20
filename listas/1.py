"""

Crear un programa que solicite al usuario ingresar un número y busque la
cantidad de ocurrencias que existen sobre una lista ya cargada.


"""
import random

lista=[]
for i in range(random.randint(10,20)):
    lista.append(random.randint(1,20))

numero=0
while numero != -1:
    numero=int(input("Ingrese numero: "))        
    print(f"El numero {numero} aparece {lista.count(numero)} veces.")
    print(lista)