"""
 En base al primer punto, luego de generar la carga de las frases, visualizar el archivo cargado.
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

try:
    with open("texto.txt","r") as archivo:
        print(archivo.read())
except OSError:
    print("Error")


finally:
    try:
        archivo.close()
    except NameError:
        print("Archivo no abierto")