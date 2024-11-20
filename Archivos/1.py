"""
Crea un programa que vaya leyendo las frases que el usuario teclea y las guarde en un 
fichero de texto llamado “frases.txt”. Terminará cuando la frase introducida sea "fin" (esa 
frase no deberá guardarse en el fichero).
"""
try:
    archivo=open("texto","at")
    print("Abierto ok")
    frase=input("Ingrese frase: ")
    while frase != "fin":
        archivo.write(frase)
        frase=input("Ingrese frase: ")
except OSError:
    print("Error")
finally:
    try:
        archivo.close()
    except NameError:
        print("Archivo no abierto")









