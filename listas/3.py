"""

Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. Luego se solicita imprimir 
los últimos 10 valores de la lista utilizando segmentación de listas.

"""
n=int(input("Ingrese numero: "))
lista=[i**2 for i in range(n)]
print(lista[-10:])