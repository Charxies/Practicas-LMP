lista=[]
listainversa=[]
def imprimir_restricciones():
    for cadena in range(5):
        s=input("introducir secuencia:")
        lista.append(s)
        n=0
        print("lista: ", lista)
    for cadena in lista:
        print(n,cadena)
        n=n+1
def invertir_lista():
    for cadena in lista:
        listainversa.append(cadena[::-1])
        n=0
        print("lista inversa", listainversa)
    for cadena in listainversa:
        print(n,cadena)
        n=n+1
imprimir_restricciones()
invertir_lista()
