"""
 Crear un programa que maneje un archivo donde se almacena la siguiente información de 
una determinada cantidad personas: Nombre, Apellido, Edad y Estatura. 
El programa deberá almacenar la información a medida que se vayan cargando. 
El formato a ser almacenado será cada dato separado por el carácter punto y coma (;) en 
el mismo orden que se carga.
Tenga en cuenta que cada vez que se ejecuta el programa, se debe incrementar el contenido 
del archivo (agregar al final).
"""

try:
    with open("personas.txt","a") as archivo:
        nombre=input("Ingrese Nombre: ")
        apellido=input("Ingrese Nombre: ")
        edad=(input("Ingrese Nombre: "))
        if len(edad)==1:
            edad=("0"+str(edad))
        estatura=(input("Ingrese Nombre: "))
        if len(estatura)==2:
            estatura=(str(estatura)+"0")
        
        archivo.write(nombre+"; "+apellido+"; "+edad+"; "+estatura+"\n")
except OSError:
    print("Error")

finally:
    archivo.close()