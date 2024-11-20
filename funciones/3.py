"""

Crear una función que reciba como parámetro un valor
numérico. En caso de que ese valor recibido
como parámetro sea múltiplo de 3, se
debe retornar el resultado de su cubo
(para calcular el cubo de dicho valor, utilizar otra
función). De no ser múltiplo de 3, retornar -1

"""

def calcularCubo(numero):
    return numero**3

def multiplo(numero):
    if numero % 3 == 0:
        return calcularCubo(numero)
    else:
        return -1
    
print(multiplo())