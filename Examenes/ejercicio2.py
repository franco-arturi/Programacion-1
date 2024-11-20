# 2) Un gimnasio quiere realizar el seguimiento del peso de sus socios. El gimnasio cuenta con 20 socios. El programa debe solicitar el nombre y el peso de cada socio. 
# Realizarlo con ciclo FOR
# Al finalizar el programa debe calcular:

# El promedio de peso de los socios
# El nombre del socio con menor peso y el valor del menor peso
# El nombre del socio con mayor peso y el valor del mayor peso


suma=0
menorPeso=None
mayorPeso=None
nombreMenorPeso=""
nombreMayorPeso=""

for i in range(1,21):

    nombre=input("Ingrese su nombre\n")
    peso=float(input("Ingrese su peso\n"))
    suma+=peso

    if menorPeso==None or peso<menorPeso:
        menorPeso=peso
        nombreMenorPeso=nombre
    
    if mayorPeso==None or peso>mayorPeso:
        mayorPeso=peso
        nombreMayorPeso=nombre


promedio=suma/20

print(f"El socio con menor peso es {nombreMenorPeso} con un peso de {menorPeso}")
print(f"El socio con mayor peso es {nombreMayorPeso} con un peso de {mayorPeso}")
print(f"El promedio de peso de socios es {promedio} ")
