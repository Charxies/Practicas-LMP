#aux salida y while para repeticion
loop=1
print("Recordatorio: el orden de ingreso de datos afecta el resultado")
def suma(numx,numy):
    return numx + numy
def resta(numx,numy):
    return numx - numy
def multiplicacion(numx,numy):
    return numx * numy
def division(numx,numy):
    return numx/numy
while loop ==1:
    numx=int(input("ingrese numero x:"))
    numy=int(input("ingrese numero y:"))
    # imprimimos opciones e ingresamos opcion
    aux = int(input("ingrese la opcion segun el indice de operaciones \n1: suma\n2: resta\n3: multiplicacion\n4: division\n5: todos los anteriores\n0: exit\n\topcion: "))
    #match cases para seleccionar opcion
    if aux == 1:
        print("suma: ",suma(numx,numy))
    elif aux == 2:
        print("resta: ",resta(numx,numy))
    elif aux == 3:
        print("multiplicacion: ",multiplicacion(numx,numy))
    elif aux == 4:
        print("division",division(numx,numy))
    elif aux == 5:
        print("suma:\t", suma(numx,numy))
        print("resta:\t",resta(numx,numy))
        print("mult:\t",multiplicacion(numx,numy))
        print("div:\t",division(numx,numy ))
    else:
        loop = 0
        break
print("fin de la aplicacion")