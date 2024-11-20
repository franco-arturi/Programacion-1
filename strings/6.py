"""

Escribir una función que reciba como parámetro una cadena de caracteres en
la que las palabras se encuentran separadas por uno o más espacios.

Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando
un espacio entre cadauna.

"""

def orden(string):
    lis=string.split()
    lis.sort()
    return " ".join(lis)

x="bsd ab zkas   yui"
print(orden(x))
    