"""
Se debe gestionar los datos de stock de una tienda de comestibles, la información a 
recoger será: nombre del producto, precio, cantidad en stock. La tienda dispone de 10 
productos distintos. El programa debe ser capaz de:
    ▪ Dar de alta un producto nuevo.
    ▪ Buscar un producto por su nombre.
    ▪ Modificar el stock y precio de un producto dado
"""
import random as r

def crearProductos():
    z={}
    n=(input("Ingrese nombre del producto: ")).title()
    z[n]={}
    z[n]["precio"]=int(input("Ingrese precio del producto: "))
    z[n]["cantidad"]=int(input("Ingrese stock del producto: "))
    return z

def main():
    prod ={'Manzana':{ 'precio': 13, 'cantidad': 7},
                'Pan':{ 'precio': 13, 'cantidad': 2},
                'Leche':{ 'precio': 13, 'cantidad': 4},
                'Queso':{ 'precio': 13, 'cantidad': 0},
                'Yogur':{ 'precio': 13, 'cantidad': 9},
                'Jugo':{ 'precio': 13, 'cantidad': 3},
                'Cereal':{ 'precio': 13, 'cantidad': 7},
                'Carne':{ 'precio': 13, 'cantidad': 5},
                'Pasta':{ 'precio': 13, 'cantidad': 0}}

    op=0
    while op != -1:
        op=int(input("Ingrese operacion a realizar:\n 1. Dar de alta producto.\n 2. Buscar producto.\n 3. Modificar info de producto. \n Opcion: "))
        if op == 1:
            prod.update(crearProductos())
        elif op == 2:
            nom=str((input("Ingrese nombre del producto: ")).title())
            if nom in prod:
                print(f"{nom} Precio: ${prod[nom].get('precio')} Stock: {prod[nom].get('cantidad')} unidades")
            else:
                print("Error")
        elif op == 3:
            nom=str((input("Ingrese nombre del producto: ")).title())
            if nom in prod:
                op_3=int(input("Cambiar:\n 1. Precio\n 2. Stock\n Opcion:"))
                if op_3==1:
                    prod[nom]['precio']=int(input("Ingrese nuevo valor del precio: "))
                elif op_3==2:
                    prod[nom]['cantidad']=int(input("Ingrese nueva cantidad de stock: "))
            else: 
                print("No existe el producto.")


        





main()