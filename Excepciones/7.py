"""
Escribe una función llamada calcularRaizCuadrada que reciba un número 
como argumento y calcule su raíz cuadrada. Si el número es negativo, 
la función debe generar una excepción ValueError con un mensaje indicando 
que no se puede calcular la raíz cuadrada de un número negativo.
"""
from math import sqrt
def calcularRaizCuadrada(num):
    if num < 0:
        raise ValueError("El numero no es positivo.")
    else:
        return sqrt(num)

while True:
    try:
        print(calcularRaizCuadrada(int(input("Ingrese numero: "))))
    except ValueError:
        print("Error numero negativo.")