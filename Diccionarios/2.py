"""
 Escriba un programa que ingrese (por teclado) los datos de diez personas (nombre, 
edad, genero, dirección, teléfono), los almacene en un diccionario y los muestre. Al 
realizar dicha muestra, destacar la persona más joven en edad.
"""
import random as r

def ingresarPersona():
    persona={"nombre":None,"edad":None,"genero":None,"direccion":None,"telefono":None}
    persona["nombre"]=input("Ingrese nombre de la persona: ")
    persona["edad"]=r.randint(1,100)
    persona["genero"]="a"
    persona["direccion"]="a"
    persona["telefono"]=12345
    print("Persona Cargada con exito!!!\n")
    return persona

def main():
    personas=[]
    mayor=0
    nombre=None
    for i in range(10):
        personas.append(ingresarPersona())
    for i in personas:
        nom,ed,gen,dir,tel=i.values()
        print(mayor)
        if ed > mayor:
            mayor = ed
            nombre = nom
        print(f"{nom}, {ed} {gen} ({dir})({tel})")
    print(f"Persona con mayor edad: {nombre}")
    

main()


