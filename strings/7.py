"""

Desarrollar una función que devuelva una subcadena con los últimos N
caracteres de una cadena dada. La cadena y el valor de N se pasan como
parámetros.


"""
def ultimosStrings(string,numero):
    return string[-1*numero-1:-1]

print(ultimosStrings("abcdefghijklmno",5))