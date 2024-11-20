"""
Se tienen dos variables del tipo diccionario, en una de ella se almacena la información 
de los artículos y la cantidad que tiene una persona en un carrito de compras:
carrito = { 
"lapiceras" : 12, 
"borrador" : 1, 
"carpeta" : 2
}
En una segunda variable, se almacenan el stock (cantidad de artículos disponibles) de 
cada uno de los artículos:
stock = {
"lapiceras" : 13, 
"borrador" : 10, 
"carpeta" : 3
}
Con relación a dicha información, se deberán elaborar las siguientes funciones: 
• hayStock(articulo, cantidad, stock): Recibe un artículo y verifica si hay stock 
disponible (retorna True en caso de que exista; False en caso contrario). 
hayStock("borrador", 1, stock) => True
hayStock("borrador", 13, stock) => False
• procesarPedido(carrito, stock): Recibe los artículos solicitados en carrito y 
realiza el descuento de stock correspondiente. Debe retornar como resultado 
el stock actualizado. No afectar la variable recibida como parámetro. Utilizando 
las variables anteriores como ejemplo, debería retornar:
{'lapiceras': 1, 'borrador': 9, 'carpeta': 1}

"""

carrito = { 
"lapiceras" : 12, 
"borrador" : 1, 
"carpeta" : 2
}

stock = {
"lapiceras" : 13, 
"borrador" : 10, 
"carpeta" : 3
}

def hayStock(art,cant, stock):
    if stock[art]>=cant:
        return True
    else:
        return False

def procesarPedido(car,sto):
    dic=sto.copy()
    for art,cant in car.items():
        dic[art]=dic[art]-cant
    return dic

print(stock)
print(procesarPedido(carrito,stock))