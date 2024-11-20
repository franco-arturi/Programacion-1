"""

 Escriba un programa para contar los números pares e impares en una lista 
dada de enteros usando Lambda.

"""
lista=[1,2,3,4,5,6,7,8,9]
contadorImpares=0
contadorPares=0
obs = (lambda z: True if z%2!=0 else False)
for i in lista:
    if obs(i)==True:
        contadorImpares+=1
    else:
        contadorPares+=1

print(contadorPares,contadorImpares)