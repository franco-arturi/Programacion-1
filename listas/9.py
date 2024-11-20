"""

Generar una lista con 50 números al azar entre 1 y 100 y crear una nueva lista con 
los elementos de la primera que sean impares. El proceso deberá realizarse utilizando 
listas por comprensión. Imprimir las dos listas por pantalla.

"""
import random as r

x=[r.randint(1,100) for i in range(50)]
y=[i for i in x if i % 2 != 0]
print(x)
print(y)