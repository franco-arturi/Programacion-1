"""
Crear un programa que permita recuperar la información del archivo generado y muestre 
los promedios de edad y estaturas. Muestre todos los datos al procesar.

"""
import re


try:
    with open("personas.txt","r") as archivo:
        linea=archivo.readline()
        cant=0
        edades=0
        estaturas=0
        patronEdades="[0-9]{2}"
        patronEstatura="[0-9]{3}"
        while not linea == "":
            print(linea)
            matchEdad=re.search(patronEdades,linea)
            matchEstatura=re.search(patronEstatura,linea)
            edades=edades + int(matchEdad.group())
            estaturas = estaturas + int(matchEstatura.group())
            cant +=1
            linea=archivo.readline()
        print(edades/cant,estaturas/cant)

except OSError:
    print("Error")

finally:
    archivo.close()