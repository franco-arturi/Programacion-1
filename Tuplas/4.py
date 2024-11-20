""" 
    Juego de cartas: crea una función que genere aleatoriamente una mano de cinco
cartas de una baraja de póker. Cada carta debe ser representada por una tupla que
contenga un número y un palo. 
"""
import random as r
def crearMano():
    aux=()
    aux=aux+(r.choice(["Picas","Corazones","Trebol","Diamantes"]),)
    aux=aux+(r.randint(1,12),)
    return aux

mano=[]
for i in range(5):
    mano.append(crearMano())
print(mano)