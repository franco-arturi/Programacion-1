"""

Crear funciones lambda que resuelvan las siguientes problemáticas:
a. Calcule la superficie de un rectángulo
b. Determine si una nota está aprobada o no (mayor o igual que 4 
aprueba). Retorna True por aprobado; False por desaprobado.
c. Que dado un número invierta su signo (de positivo a negativo y 
viceversa)
d. Que dado un nombre determine si su longitud es larga (mayor de 10 
caracteres). Retorna True o False.
e. Dado un valor numérico retorne True si es positivo o cero; False en 
caso contrario.
f. Escribe una función que tome dos argumentos: a y b y devuelva la 
multiplicación de ellos.
g. Que compare dos valore

"""

area = (lambda base,altura: base*altura)
aprobado = (lambda nota: True if nota >= 4 else False )
inversor = (lambda numero: numero*-1)
longitud = (lambda string: True if len(string)>10 else False)
signo = (lambda numero: True if numero >= 0 else False)
multi = (lambda a,b: a*b)
igualdad = (lambda a,b: True if a==b else False)

print(())

