class Vehiculo:
    marca: str
    modelo: str

    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def mostrarInformacion(self):
        print(f"Vehiculo marca {self.marca}, modelo {self.modelo}.")

class Auto(Vehiculo):
    puertas: int
    def __init__(self, marca: str, modelo: str, puertas: int):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def mostrarInformacion(self):
        print(f"Auto marca {self.marca}, modelo {self.modelo} con {self.puertas} puertas.")

class Moto(Vehiculo):
    tipo: str
    def __init__(self, marca: str, modelo: str, tipo: str):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def mostrarInformacion(self):
        print(f"Moto {self.tipo}, marca {self.marca}, modelo {self.modelo}.")

v1 = Vehiculo("Ford", "F150")
a1 = Auto("Toyota", "Corolla", 4)
m1 = Moto("Yamaha", "D1", "Deportiva")

v1.mostrarInformacion()
a1.mostrarInformacion()
m1.mostrarInformacion()