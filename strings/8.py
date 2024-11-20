"""

Desarrollar una función para reemplazar todas las apariciones de una palabra
por otra en una cadena de caracteres y devolver la cadena obtenida y un
entero con la cantidad de reemplazos realizados.
Tener en cuenta que sólo
deben reemplazarse palabras completas, y no fragmentos de palabras.
Escribir también un programa para verificar el comportamiento de la función.


"""

def reemplazo(string,vieja,nueva):
    lis=string.split()
    cont=0
    while vieja in lis:
        cont +=1
        lis[lis.index(vieja)]=nueva
    return " ".join(lis),cont


x="hola ola q tal me llamo ola"
print(reemplazo(x,"ola","Juan"))

