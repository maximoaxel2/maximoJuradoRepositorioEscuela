class Libro:
    titulo: str
    autor: str
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def informacion(self):
        print(f"Libro {self.titulo} por {self.autor}.")

class LibroDigital(Libro):
    formato: str

    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.formato = formato
    def informacion(self):
        print(f"Libro {self.titulo} por {self.autor} en formato {self.formato}.")
        
class LibroFisico(Libro):
    paginas: int

    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo, autor)
        self.paginas = paginas
    def informacion(self):
        print(f"Libro {self.titulo} por {self.autor} con {self.paginas} paginas.")

l1 = Libro("1984", "George Orwell")
eB1 = LibroDigital("Twenty Thousand Leagues Under the Sea", "Jules Verne", "ePub")
fB1 = LibroFisico("El color de la magia", "Terry Pratchett", 288)

l1.informacion()
eB1.informacion()
fB1.informacion()