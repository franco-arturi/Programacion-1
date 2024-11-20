"""
Contador de palabras: Escribe un programa que lea un archivo de texto y cuente la 
cantidad de veces que aparece cada palabra en el archivo. Utiliza un diccionario para 
almacenar las palabras y sus frecuencias. Al final, muestra las 10 palabras más comunes 
en el archivo.

"""
contador={}
arch = open(r"C:\Users\Usuario1\Desktop\Programacion\Facultad\Programacion 1\Practica\Diccionarios\texto.txt",'r') 
texto=arch.read().split()
arch.close()
for i in texto:
    if i in contador:
        contador[i]+=1
    elif i not in contador:
        contador[i]=1

conLista=dict((sorted(list(contador.items()),key=lambda x: x[1],reverse=True))[:10])
print(conLista)



