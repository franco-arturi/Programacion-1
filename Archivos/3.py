"""
 Crear un archivo que se llame “montos.txt”, en el mismo se almacenarán valores numéricos. 
Realizar un proceso que visualice su contenido y, al finalizar, muestre el total (sumatoria de 
los valores) y promedio.
"""
try:
    with open("montos.txt","r") as archivo:
        num=0
        cont=0
        sum=int(archivo.readline())
        while sum != "":
            num=num+int(sum)
            cont += 1
            sum=(archivo.readline())
        print(num)
        print(num/cont)
        

except OSError:
    print("error")

finally:
    archivo.close()