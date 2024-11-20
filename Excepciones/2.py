"""
Realizar una función que reciba como parámetros dos cadenas de  caracteres 
conteniendo números reales, sume ambos valores y devuelva el resultado como un número real. 
Devolver None si alguna de las cadenas no contiene un número válido, utilizando manejo de 
excepciones para detectar el error.
"""
def func(cad1,cad2):
    try:
        return(int(cad1)+int(cad2))
    except TypeError:
        print("Tipo de dato erroneo, debe ingresar exlucisvamente numeros.")
        return None


func('123','aa')