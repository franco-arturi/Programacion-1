"""

Contar el número de vocales: Crea un programa que le pida al usuario que
ingrese una cadena y luego cuente y muestre el número de vocales que hay
en la cadena. Ayuda: Puedes usar un bucle for para recorrer la cadena y un
condicional if para comprobar si cada carácter es una vocal.


"""
vocales=["a","e","i","o","u"]
x=str(input("Ingrese una cadena de texto: "))
cont=0
for i in x:
    if i in vocales:
        cont += 1
print(x,cont)