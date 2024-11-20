""" 
 Crear una variable utilizando tuplas que sea capaz de almacenar los valores de las
cartas de la baraja española (48 cartas; del 1 al 12 de basto, copa, espada y oro).
    a. Crear una función que retorne una lista con una determinada cantidad de
    cartas seleccionadas al azar que será recibida como parámetro (junto con la
    variable que se creó el mazo).
    b. b. Utilizando la función anterior, obtenga 10 cartas del mazo e indique la
    cantidad de cartas que son de oro    
"""
import random as r

baraja_espanola = (
    ('Basto', 1), ('Basto', 2), ('Basto', 3), ('Basto', 4), ('Basto', 5), 
    ('Basto', 6), ('Basto', 7), ('Basto', 8), ('Basto', 9), ('Basto', 10), 
    ('Basto', 11), ('Basto', 12),
    ('Copa', 1), ('Copa', 2), ('Copa', 3), ('Copa', 4), ('Copa', 5), 
    ('Copa', 6), ('Copa', 7), ('Copa', 8), ('Copa', 9), ('Copa', 10), 
    ('Copa', 11), ('Copa', 12),
    ('Espada', 1), ('Espada', 2), ('Espada', 3), ('Espada', 4), ('Espada', 5), 
    ('Espada', 6), ('Espada', 7), ('Espada', 8), ('Espada', 9), ('Espada', 10), 
    ('Espada', 11), ('Espada', 12),
    ('Oro', 1), ('Oro', 2), ('Oro', 3), ('Oro', 4), ('Oro', 5), 
    ('Oro', 6), ('Oro', 7), ('Oro', 8), ('Oro', 9), ('Oro', 10), 
    ('Oro', 11), ('Oro', 12)
)

def listaCartas(tup,cant):
    lis=[]
    for i in range(cant):
        lis.append(r.choice(tup))
    return lis

cartas=listaCartas(baraja_espanola,10)
cant=0
for i in cartas:
    if i[0]=='Oro':
        cant+=1
print(cartas)
print(cant)

