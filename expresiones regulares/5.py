"""
Escribe un programa que encuentre todas las apariciones de números en una 
cadena y devuelva cada número encontrado en una lista. Utilice el método 
finditer para su resolución
"""
import re
x=0
while x!="": 
    y = input("Ingrese string: ")
    match = (re.finditer(r"\d+",y))
    for i in match:
        print(f"{i.group()} ")
    x=(input("Ingrese: "))