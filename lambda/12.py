"""

Crea una función ordenaPalabras que acepte una lista de palabras como argumento, 
y devuelva una nueva lista con las palabras ordenadas alfabéticamente en orden inverso. 
Utiliza funciones lambda, map y sorted para implementarla.

"""

def ordenPalabras(lis):
    aux=sorted(lis,reverse=True)
    return aux
x=(str(input("Texto: "))).split()
print(ordenPalabras(x))