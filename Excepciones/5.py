"""
 Escribir un programa que juegue con el usuario a adivinar un número. 
 El programa debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. 
 Para eso, cada vez que se introduce un valor se muestra un mensaje indicando si el 
 número que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga adivinarlo, 
 se debe imprimir en pantalla la cantidad de intentos que le tomó hallar el número. 
 Si el usuario introduce algo que no sea un número se mostrará un mensaje en pantalla y 
se lo contará como un intento más.
"""

import random as r

def intento(num):
    try:
        adi=int(input("Ingrese numero: "))
        if num == adi:
            return True
        elif num>adi:
            print(f'El numero es mayor a {adi}.')
            return False
        elif num<adi:
            print(f'El numero ed menor a {adi}.')
            return False
        

    except ValueError:
        print('El valor no es numerico, cuenta como intento, intentar nuevamente: ')
        return False


def main():
    num=r.randint(1,500)
    victoria=False
    contador=0
    while victoria == False:
        victoria=intento(num)
        contador+=1
    print(f'Victoria, intentos {contador}')


main()