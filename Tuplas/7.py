""" 
Cálculo de áreas: crea un programa que lea una lista de tuplas, donde cada tupla
contiene el nombre de una figura geométrica (cuadrado, rectángulo, triángulo y
círculo) y sus dimensiones, y calcule el área de cada figura    
"""

figuras=[('cuadrado',2,2),('circulo',12),('triangulo',2,1),('rectangulo',3,2)]
for i in figuras:
    if i[0]=='cuadrado' or i[0]=='rectangulo':
        print(f'El area del {i[0]} es {i[1]*i[2]} ')
    elif i[0]=='circulo':
        print(f'El area del {i[0]} es {( i[1]*i[1]*3.14)} ')
    elif i[0]=='triangulo':
        print(f'El area del {i[0]} es {(i[1]*i[2])/2} ')