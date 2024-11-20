"""
 Realice un programa que pida datos de personas: nombre, día de nacimiento, mes de 
nacimiento, y año de nacimiento. Después deberá repetir lo siguiente: preguntar un 
número de mes y mostrar en pantalla los datos de las personas que cumplan los años 
durante ese mes. Terminará de repetirse cuando se teclee vacío en el nombre. Persista 
y recupere la información en cada ejecución en un archivo llamado cumpleaños.json.
"""

import random as r
def crearPersona():
    x={}
    x["dni"]=r.randint(0000,9999)
    x["dia"]=r.randint(1,30)
    x["mes"]=r.randint(1,12)
    x["año"]=r.randint(1910,2024)
    return x
def main():
    y=[]
    for i in range(15):
        y.append(crearPersona())
        opcion = 0
    while opcion != -1:
        opcion=int(input("Ingrese mes a buscar: "))
        for i in y:
            if i["mes"] == opcion:
                dni=i["dni"]
                dia=i["dia"]
                mes=i["mes"]
                año=i["año"]
                print(f"DNI: #{dni} {dia}/{mes}/{año}")


main()