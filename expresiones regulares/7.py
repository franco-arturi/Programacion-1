"""

Escribe una función que extraiga todos los hashtags de una cadena dada. Un 
hashtag se define como cualquier secuencia de caracteres alfanuméricos 
precedida por un símbolo # y puede contener letras, números y guiones 
bajos. La función debe devolver una lista con todos los hashtags encontrados 
en la cadena.

"""

import re 

def extraerHash(string):
    patron=r"#\w+"
    match = re.finditer(patron,string)
    return match
x=(extraerHash("#afd #90afsdf 24#sdf2"))
for i in x:
    print(i.group())