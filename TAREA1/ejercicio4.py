restricciones={
    "GAATTC","CGATCC", "AAGCTT"
}


def imprimir_restricciones():
    for restriccion in restricciones:
        s=input("introducir secuencia:")
        print(s, " es una zona restringida: ",s in restricciones)

imprimir_restricciones()