"""
Juego de adivinanza de frutas: Crea un diccionario con nombres de frutas como claves y 
sus descripciones como valores. El programa debe elegir aleatoriamente una fruta y 
mostrar su descripción. Luego, el usuario debe adivinar qué fruta es. Si el usuario adivina 
correctamente, el programa debe mostrar un mensaje de felicitación.
"""
import random as r

frutas = {
    "Manzana": "Fruta dulce y crujiente, generalmente de color rojo, verde o amarillo.",
    "Banana": "Fruta alargada y curvada, de color amarillo cuando está madura.",
    "Naranja": "Fruta cítrica de color naranja, conocida por su alto contenido de vitamina C.",
    "Fresa": "Pequeña fruta roja con semillas en su superficie, dulce y jugosa.",
    "Uva": "Pequeña fruta redonda, puede ser de color verde, rojo o morado, utilizada para hacer vino.",
    "Piña": "Fruta tropical grande con una piel dura y espinosa, y una pulpa dulce y jugosa.",
    "Mango": "Fruta tropical de color amarillo o rojo, con una pulpa dulce y jugosa.",
    "Kiwi": "Pequeña fruta marrón con una pulpa verde brillante y un sabor agridulce.",
    "Sandía": "Gran fruta verde con una pulpa roja y jugosa, ideal para el verano.",
    "Cereza": "Pequeña fruta redonda y roja, dulce y jugosa, con un hueso en el centro."
}

op = 0
while op != 1:
    actual = (str(r.choices(list(frutas.keys())))).strip("[]''")
    print("PISTA: ")
    print(f"{frutas[actual]}")
    eleccion=(input("Ingrese nombre de la fruta: ")).title()
    if eleccion == actual:
        print("Felicidades, respuesta correcta!!!")
        op = 1
    else: 
        print("Siga intentando...")
    