"""
Crear dos archivos:
.: Paises.txt → Con el contenido de los países de Latinoamérica
.: Provincias.txt → Con el contenido de las provincias de Argentina
Crear un programa que le pregunte al usuario si quiere ver los países o provincias, de 
acuerdo a su selección, debe mostrar su contenido en pantalla (que elija 1 o 2 con el teclado).
"""

op=int(input("Que se desea ver, provincias de Argentina(1) o paises de Latino America(2)?: "))
if op ==1:
    try: 
        with open("Provincias.txt","r") as archivo:
            print(archivo.read())
    except OSError:
        print("ERROR")
    finally:
        archivo.close()
elif op == 2:
    try: 
        with open(r"Paises.txt","r") as archivo:
            print(archivo.read())
    except OSError:
        print("ERROR")
    finally:
        archivo.close()