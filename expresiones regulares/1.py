"""

Escriba  un  programa  que  busque  la  palabra  "python"  
en  una  cadena ingresada por el usuario, 
sin importar que sea mayúsculas o minúsculas. 
Utilice el método findall para resolverlo. 

"""
import re
x=0
while x!=-1:
    
    cadena = input("Ingrese un string: ")
    patron = "python"
    match = re.findall(patron,cadena,re.IGNORECASE)
    if match:
        print("Bien")
    else:
        print("Mal")
    x=int(input("Seguir: "))
    
