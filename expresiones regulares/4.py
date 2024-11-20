"""

Desarrolle una función que busque la existencia de una palabra en una 
cadena, sin importar mayúsculas o minúsculas. De ser así, retornará True; 
False en caso contrario. Utilice el método search para su resolución.


"""

import re

def encontrarInstancia(string,patron):
    match = re.search(patron,string,re.IGNORECASE)
    if match:
        return True
    else:
        return False

x=0
while x!="": 
    print(encontrarInstancia((input("Ingrese string: ")),(input("Ingrese patron: "))))
    x=(input("Ingrese: "))
