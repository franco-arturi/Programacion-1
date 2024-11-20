"""
Escribe un programa que lea un archivo CSV con información sobre ventas de una tienda
(los valores serán fecha, producto, precio, cantidad por cada fila; por ejemplo: 
01/01/2023,Pantalones,50,10). El programa debe calcular el total de ventas por día.
"""
import re
try:
    with open(r"ventas.csv","r") as archivo:
        ventas={}
        linea=archivo.readline()
        while linea != "":
            
            patronFecha="[0-9]{2}/[0-9]{2}/[0-9]{4}"
            patronPrecio=r"\$[0-9]{1,}"
            patronCantidad=r"\d+$"
            fechaMatch=re.search(patronFecha,linea)
            precioMatch=re.search(patronPrecio,linea)
            cantMatch=re.search(patronCantidad,linea)
            if fechaMatch.group() in ventas:
                ventas[fechaMatch.group()] += int (precioMatch.group()[1:])* int(cantMatch.group())
            else:
                ventas[fechaMatch.group()] = int(precioMatch.group()[1:])* int(cantMatch.group())
            linea=archivo.readline()
        
        
        print(fechaMatch.group())
        print(precioMatch.group()[1:])

        print(ventas)
        
except OSError:
    print("ERROR")

finally:
    archivo.close()