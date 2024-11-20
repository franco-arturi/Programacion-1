"""

Escribir una función filtrarPalabras() que reciba una cadena de caracteres
conteniendo una frase y un entero N, y devuelva otra cadena con las
palabras que tengan N o más caracteres de la cadena original. Escribir
también un programa para verificar el comportamiento de la misma.


"""

def filtrarPalabras(string,numero):
    lista=string.split()
    nuevaLista=[]
    for i in lista:
        if len(i) >= numero:
            nuevaLista.append(i)
    return " ".join(nuevaLista)

x="a bcd ds jajajaj si jklñ"

print(type(filtrarPalabras(x,3)))

