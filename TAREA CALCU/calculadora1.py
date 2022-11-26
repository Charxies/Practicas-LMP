#aux salida y while para repeticion
loop=1
print("Recordatorio: el orden de ingreso de datos afecta el resultado")
while loop ==1:
    numx=int(input("ingrese numero x:"))
    numy= int(input("ingrese numero y:"))
    suma=numx+numy
    resta=numx-numy
    multiplicacion=numx*numy
    division=numx/numy
    # imprimimos opciones e ingresamos opcion
    aux = int(input("ingrese la opcion segun el indice de operaciones \n1: suma\n2: resta\n3: multiplicacion\n4: division\n5: todos los anteriores\n0: exit\n\topcion: "))
    #match cases para seleccionar opcion
    if aux == 1:
        print("suma: ",suma)
    elif aux == 2:
        print("resta: ",resta)
    elif aux == 3:
        print("multiplicacion: ",multiplicacion)
    elif aux == 4:
        print("division",division)
    elif aux == 5:
        print("suma:\t", suma)
        print("resta:\t",resta)
        print("mult:\t",multiplicacion)
        print("div:\t",division)
    else:
        loop = 0
        break
print("fin de la aplicacion")