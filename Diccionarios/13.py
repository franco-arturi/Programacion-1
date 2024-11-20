"""
En un sistema de recetas de cocinas, se tiene dos variables. En una de ellas, se 
almacena en un conjunto la información de los ingredientes que tiene una persona en 
su casa a disposición:
ingredientes = { "huevo", "aceite", "papas"}
En una segunda variable, se encuentran parametrizadas las recetas existentes 
indicando que ingredientes se requieren para cada preparación:
recetas = {
 "Papas fritas" : { "aceite", "papas" },
 "Huevo frito" : { "huevo", "aceite" },
 "Pure de papas" : { "papas", "manteca" }
}
Conociendo dicha información, se deberán elaborar las siguientes funciones (que 
deben incluir dentro de la misma operaciones de conjunto en su resolución): 
 
• recetasPosibles (ingredientes, recetas), que retorne una lista con el nombre de 
las recetas que son posibles de realizar con los ingredientes indicados. 
Resultado esperado con los ejemplos dados:
['Papas fritas', 'Huevo frito']
• ingredientesFaltantes (ingredientes, recetas), que retorne un diccionario 
donde, por cada receta existente, indique la lista de ingredientes faltantes para 
realizar la receta. Si no falta ningún ingrediente, debería mostrarse la lista 
vacía. Resultado esperado con los ejemplos dados:
{'Papas fritas': [], 'Huevo frito': [], 'Pure de papas': ['manteca']
"""

ingredientes = { "huevo", "aceite", "papas"}
recetas = {
 "Papas fritas" : { "aceite", "papas" },
 "Huevo frito" : { "huevo", "aceite" },
 "Pure de papas" : { "papas", "manteca" }
}

def recetasPosibles(ing,re):
    lis=[]
    for nom,ingre in re.items():
        if not ingre-ing:
            lis.append(nom)
    return lis

def ingredientesFaltantes(ing,re):
    faltantes={}
    for nom,ingre in re.items():
        faltantes[nom]=list(ingre-ing)
    return faltantes



print(ingredientesFaltantes(ingredientes,recetas))