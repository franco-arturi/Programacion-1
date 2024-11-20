"""
Escribe una función para verificar si una cadena comienza con una letra 
mayúscula. De ser así, retornará True; False en caso contrario. Utilice el 
método match para su resolución.
"""
import re

def comienzoMayus(string):
    patron="^[A-Z]"
    match = re.match(patron, string)
    if match:
        return True
    else: 
        return False
x=0
while x!="": 
    print(comienzoMayus(input("Ingrese string: ")))
    x=(input("Ingrese: "))
