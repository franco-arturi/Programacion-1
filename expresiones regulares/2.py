"""
Escriba un programa que busque todas las letras mayúsculas en una cadena 
ingresada por el usuario e imprima cada una de ellas. Utilice el método 
findall para resolverlo.
"""

import re
cadena = input("Ingrese un string: ")
patron = "[A-Z]"
match = re.findall(patron,cadena)
print(match)
