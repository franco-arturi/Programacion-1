"""
 Genere un programa que pregunte un nombre de archivo (ubicación) y muestre en pantalla 
el contenido de ese archivo. Informe en pantalla si no existe
"""
nombre=((input("Ingrese direccion del archivo:  ")))
try:
    with open((nombre),"r") as archivo:
        print(archivo.read())
except OSError as e:
    print("Archivo no existente")
finally:

    try: archivo.close()
    except:
        print("Error, archivo no abierto.")