class transporte:
    def __init__(self, gasolina, marca, modelo, estado):
        self.gasolina = gasolina
        self.marca = marca
        self.modelo = modelo
        self.estado = estado

    def encender(self):
        if self.gasolina > 1:
            print("encendido")
            self.estado = 1
        else:
            print("no hay gasolina")
            self.estado = 0

    def apagar(self):
        print("apagar")
        self.estado = 0

    def avanzar(self):
        if self.estado != 0 and self.gasolina > 0:
            print("avanzando")
            self.gasolina = self.gasolina - 1
            print(f"gasolina: {self.gasolina}")
        else:
            print("no se puede avanzar")
            if self.estado == 0:
                print("no se ha encendido")
            elif self.gasolina == 0:
                print("no hay gasolina")
            else:
                print("error inesperado")

    def __str__(self):
        return f" gas:{self.gasolina},{self.marca},{self.modelo}"


class Automovil(transporte):
    def __init__(self, gasolina, marca, modelo, estado, color, placa):
        super().__init__(gasolina, marca, modelo, estado)
        self.color = color
        self.placa = placa

    def vueltaIzq(self):
        if self.estado != 0 and self.gasolina > 0:
            print("Vuelta a la izquierda")
            self.gasolina = self.gasolina - 1
            print(f"gasolina: {self.gasolina}")

        else:
            print("no se puede dar vuelta")
            if self.estado == 0:
                print("no se ha encendido")
            elif self.gasolina == 0:
                print("no hay gasolina")
            else:
                print("error inesperado")

    def vueltaDer(self):
        if self.estado != 0 and self.gasolina > 0:
            print("Vuelta a la derecha")
            self.gasolina = self.gasolina - 1
            print(f"gasolina: {self.gasolina}")
        else:
            print("no se puede dar vuelta")
            if self.estado == 0:
                print("no se ha encendido")
            elif self.gasolina == 0:
                print("no hay gasolina")
            else:
                print("error inesperado")

    def __str__(self):
        return f"{transporte.__str__(self)},{self.color},{self.placa}"


class Avion(transporte):
    def volar(self):
        if self.estado != 0 and self.gasolina > 0:
            print("volando")
            self.gasolina = self.gasolina - 10
            print(f"gasolina: {self.gasolina}")

        else:
            print("no se puede volar")
            if self.estado == 0:
                print("no se ha encendido")
            elif self.gasolina == 0:
                print("no hay gasolina")
            else:
                print("error inesperado")


class Tren(transporte):
    @staticmethod
    def pitar():
        print("pitando \n BWOOOOOOOOMP BWOOOOOOOOMP")
