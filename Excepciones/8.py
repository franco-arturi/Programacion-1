"""
Escribe un programa que pida al usuario que ingrese dos números enteros y muestre 
el resultado de la división del primer número por el segundo. 
Si el segundo número es cero, muestra un mensaje de error y vuelve a solicitar el segundo número hasta 
que sea diferente de cero. 
Lo mismo si el tipo de dato ingresado no es correcto. 
Con cada intento de realizar la operación se debe mostrar en pantalla la leyenda: 
«Se ha intentado realizar una división».
"""
estado = True
while estado == True:
    try:
        x=int(input('Ingrese: '))
        y=int(input('Ingrese: '))

        if y==0:
            raise ValueError('Error, numero no puede ser 0')
        else:
            print(x/y)
            estado=False
    except ValueError:
        print('Se ha intentado realizar una división')
