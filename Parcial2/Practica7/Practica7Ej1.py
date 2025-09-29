class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, escuela):
        super().__init__(nombre, edad)
        self.escuela = escuela

    def estudiar(self):
        print(f"{self.nombre} esta estudiando en {self.escuela}.")

e1 = Estudiante("Ana", 20, "Preparatoria #5")
e1.saludar()
e1.estudiar()