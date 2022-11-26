import json
from collections import Counter

arch1=open("perro.txt", "r")
arch2=open("doc.txt", "w")
#print(arch1.readline())
def contadorpalabras():
    diccionario = dict()
    diccionariomin = dict()
    for linea in arch1:
        linea = linea.strip()
        linea = linea.lower()
        palabras = linea.split()
        for palabra in palabras:
            if palabra in diccionario:
                diccionario[palabra] += 1
            else:
                diccionario[palabra] = 1
    for palabra in diccionario:
        diccionariomin[palabra] = diccionario[palabra]
    return diccionariomin



palabrasRep = contadorpalabras()
print(palabrasRep)
print("-------------\n"
      "las 5 palabras mas repetidas son:" )
print(dict(Counter(palabrasRep).most_common(5)))
with open('doc.txt', 'w') as f:
    f.write(f"palabras repetidas en orden por repeticion:\n")
    f.write(json.dumps(dict(Counter(palabrasRep).most_common(len(palabrasRep)))))
print("--------------"
      "\n archivo escrito")


