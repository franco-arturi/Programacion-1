"""

Eliminar caracteres: Crea un programa que le pida al usuario que ingrese
una cadena y luego elimine todas las ocurrencias de un carácter específico
en la cadena. Por ejemplo, puedes pedirle al usuario que ingrese una cadena
y luego eliminar todas las letras "a".

"""

x=str(input("Ingrese string: "))
y=[]
caracter="a"
for i in x:
    y.append(i)
while caracter in y:
    y.remove(caracter)

print("".join(y))