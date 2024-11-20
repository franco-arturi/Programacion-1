"""
Desarrollar una función que devuelva una cadena de caracteres con el nombre 
del mes cuyo número se recibe como parámetro. Los nombres de los meses 
deberán obtenerse de una tupla de cadenas de caracteres inicializada dentro 
de la función. Devolver una cadena vacía si el número de mes es inválido. 
La detección de meses inválidos deberá realizarse a través de excepciones.
"""

def func(mes):
    try:
        meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
        return meses[mes-1]
    except IndexError:
        return ""

print(func(-1))
        