# 1) Leer números que representan temperaturas en diferentes ciudades hasta que se ingrese el valor 999. 
# Para cada ciudad evaluar si la temperatura cumple con una de las siguientes condiciones:

# Si la temperatura es mayor a 30 y menor o igual a 50, marcarla como una temperatura alta
# Si la temperatura está entre 0 y 30 inclusive o es igual a -1 marcarla como temperatura moderada
# Si la temperatura es menor a 0 y no es igual a -1 marcarla como una temperatura negativa

# Al finalizar imprimir:

# Cuantas ciudades registraron temperaturas altas
# Cuantas ciudades registraron temperaturas moderadas
# Cuantas ciudades registraron temperaturas negativas


cantTempAltas=0
cantTempModeradas=0
cantTempNegativas=0


bandera=True 

while bandera:

    temperatura=float(input("Ingrese una temperatura\n"))

    if temperatura==999:
        bandera=False
    else:
        if temperatura>30 and temperatura<=50:
            cantTempAltas+=1
        elif (temperatura>=0 and temperatura<=30) or temperatura==-1:
            cantTempModeradas+=1
        elif temperatura<0 and temperatura!=-1:
            cantTempNegativas+=1


print(f"La cantidad de ciudades que registraron temperaturas altas son {cantTempAltas}")
print(f"La cantidad de ciudades que registraron temperaturas moderadas son {cantTempModeradas}")
print(f"La cantidad de ciudades que registraron temperaturas negativas son {cantTempNegativas}")
        