"""
 Desarrollar una función para ingresar a través del teclado un número. 
 La función rechazará cualquier ingreso inválido de datos utilizando excepciones y 
 mostrará la razón exacta del error. Devolver el valor ingresado cuando éste sea correcto. 
 Escribir también un programa que permita probar el correcto funcionamiento de la misma.
"""



def algo():
    try:
        x=int(input("Ingrese numero: "))
        print("Bien")
    except ValueError as e:
        print(f"Error: {e}")


algo()