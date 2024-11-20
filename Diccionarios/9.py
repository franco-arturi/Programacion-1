"""
Supongamos que un coleccionista de figuras Funko Pop de Rick y Morty tiene un carrito 
de compras con las siguientes figuras y sus respectivas cantidades:
carrito = { 
 "Rick Sanchez" : 2, 
 "Morty Smith" : 3, 
 "Summer Smith" : 1,
 "Mr. Meeseeks" : 4
}
Y además, el coleccionista conoce los precios unitarios (en dólares) de estas figuras:
precios = {
 "Rick Sanchez" : 15, 
 "Morty Smith" : 12,
 "Summer Smith" : 10,
 "Mr. Meeseeks" : 20
}
Cree una función llamada precioTotal que calculará el monto total de la compra en 
función de estos datos. Cuando se llame a la función precioTotal(carrito, precios) con los 
diccionarios proporcionados, se debe obtener el monto total de la compra basado en la 
multiplicación de la cantidad de cada figura por su precio unitario en dólares.

"""
precios = {
 "Rick Sanchez" : 15, 
 "Morty Smith" : 12,
 "Summer Smith" : 10,
 "Mr. Meeseeks" : 20
}
carrito = { 
 "Rick Sanchez" : 2, 
 "Morty Smith" : 3, 
 "Summer Smith" : 1,
 "Mr. Meeseeks" : 4
}

def precioTotal(dicPrecios,dicCarrito):
    total=0
    for nombre,cantidad in dicCarrito.items():
        total=total+cantidad*dicPrecios[nombre]
    return total

print(precioTotal(precios,carrito))