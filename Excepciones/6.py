"""
Convertir una cadena en un número: Escribe un programa que solicite 
al usuario una cadena y luego intente convertirla en un número entero. 
Si la conversión falla, muestra un mensaje de error.
"""


try:
    x=str(input('Ingrese numero: '))
    print(int(x))

except ValueError:
    print('Error.')