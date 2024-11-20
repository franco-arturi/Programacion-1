"""

Desarrollar una función que determine si una cadena de caracteres es
capicúa. Escribir además un programa que permita verificar su
funcionamiento solicitándole al usuario valores hasta que el mismo sea vacío.

"""

def stringCapicua(string):
    if string == string[::-1]:
        return (True)
    else:
        return (False)


stringCapicua("")