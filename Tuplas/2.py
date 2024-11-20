""" 
Escribir un programa que dadas dos tuplas de tres elementos, realice el producto de
cada elemento existente en la primera tupla con todos los restantes del segundo y
almacene cada resultado en otra tupla.
Por ejemplo, el producto escalar entre (1, 2, 3) y (4, 5, 6); debería retornar: ((4, 5,
6),(8, 10, 12), (12, 15, 18)).
   
"""

tup1=(1,2,3)
tup2=(4,5,6)
tupFinal=()
for i in tup1:
    aux=[]
    for j in tup2:
        aux.append(i*j)
    tupFinal+=(tuple(aux),)
    

print(tupFinal)