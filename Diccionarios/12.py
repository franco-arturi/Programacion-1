"""
 En una tienda que confecciona banderas de países de tela, se tiene en su programa dos 
variables para cumplir su objetivo, en una de ella se almacena la información de 
colores de las telas que se tienen a disposición dentro de un conjunto:
colores = { "azul", "blanco", "rojo"}
Y, en una segunda variable, los colores necesarios para confeccionar las banderas de 
los diferentes países:
banderas = {
 "Argentina" : { "blanco", "celeste" },
 "Francia" : { "azul", "blanco", "rojo"},
 "Polonia" : { "blanco", "rojo"}
}
En función de dicha información, deberá elaborar las siguientes funciones (utilice 
dentro de las mismas operaciones de conjuntos para lograr el resultado): 
 
• banderasPosibles(colores, banderas), que retorne una lista con el nombre de 
las banderas que son posibles de realizar con los colores indicados. Siguiendo 
los ejemplos brindados, debería retornar lo siguiente:
['Francia', 'Polonia']
• coloresFaltantes (colores, banderas), que retorne un diccionario donde por 
cada bandera existente indique la lista de colores faltantes para realizarla. Si no 
falta ningún color, debería mostrarse la lista vacía. En relación a los ejemplos 
brindados, este debería ser el resultado del llamado de la función:
{
'Argentina': ['celeste'], 
'Francia': [], 
'Polonia': []
}

"""

colores = { "azul", "blanco", "rojo"}
banderas = {
 "Argentina" : { "blanco", "celeste" },
 "Francia" : { "azul", "blanco", "rojo"},
 "Polonia" : { "blanco", "rojo"}
}

def banderasPosibles(col,ban):
    posibilidades=[]
    for nom,elem in ban.items():
        if elem & col == elem:
            posibilidades.append(nom)
    return posibilidades

def coloresFaltantes(col,ban):
    faltantes={}
    for nom,elem in ban.items():
        faltantes[nom]=list(elem-col)
    return faltantes

print(coloresFaltantes(colores,banderas))