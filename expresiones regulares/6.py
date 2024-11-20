"""

Escriba una función que reemplace todas las vocales en una cadena con el 
carácter '_'. Utilice el método sub para el desarrollo

"""
import re

def remplazar(string):
    patron = "[a,e,i,o,u,A,E,I,O,U]"
    return re.sub(patron,"_",string)

print(remplazar("hola mi nombre es jasdadajsd"))