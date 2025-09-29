class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido.")

class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} hace guau guau.")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} hace miau miau.")

p1 = Perro("Firulais")
g1 = Gato("Michi")

p1.hacer_sonido()
g1.hacer_sonido()