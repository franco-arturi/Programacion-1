"""

Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada
en forma ascendente o False en caso contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y 
ordenada(['b', 'a']) retorna False. Desarrollar además un programa para verificar el comportamiento de la función.

"""

def chequeoOrden(l1):
    print(f"Lista original: {l1}")
    print(f"Lista ordenada: {sorted(l1)}")
    if l1 == sorted(l1):
        return True
    else:
        return False

x=[1,2,3,4]
y=[1,3,2,4]

sorted
print(chequeoOrden(y))