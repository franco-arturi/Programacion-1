"""
 Desarrolle un programa que almacene datos de canciones en formato MP3: 
Artista, Título, Duración (en segundos), Tamaño del fichero (en KB). Un programa 
debe pedir los datos de una canción al usuario y después mostrarlos en pantalla. 
Debe interrumpirse la carga cuando el artista ingresado sea vacío
"""
canciones=[{"artista":"Nombre","Titulo":"Nombre","Duracion":12334,"tamaño":2343}]
artista=input("Ingrese nombre del artista: ")

while artista != "":
    diccionario={}
    titulo=input("Ingrese nombre de la cancion: ")
    duracion=int(input("Ingrese duracion de la cancion en segundos: "))
    tamaño=int(input("Ingrese tamaño del archivo: "))
    diccionario[artista]=artista
    diccionario[titulo]=titulo
    diccionario[duracion]=duracion
    diccionario[tamaño]=tamaño
    for valor, key in diccionario.items():
        print(valor," es ",key)
    canciones.append(diccionario)
    artista=input("Ingrese nombre del artista: ")

