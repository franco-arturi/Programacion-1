"""

Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 
7 que no sean múltiplos de 5. A y B se ingresan desde el teclado.

"""
a=int(input("Ingrese numero: "))
b=int(input("Ingrese numero: "))
x=[i for i in range(a,b) if i%7==0 if i%5!=0]
print(x)
