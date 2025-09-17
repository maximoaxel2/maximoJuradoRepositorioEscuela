# Maximo Jurado
from typing import Callable, Any

class MenuOption:
    name : str = "-def"
    method : Callable[[Any], Any] | None = lambda : print(f"Esta opcion no tiene un metodo definido.")
    
    def __init__(self, name : str , method : Callable[[Any], Any] | None = None):
        self.name = name
        self.method = method
        menuOptions.append(self)

    def __call__(self, *args, **kwds):
        self.method()

menuOptions : list[MenuOption] = []

class InputHandler:
    lastInput : str | int | bool | float = -1
    lastInputRaw : str = ""

    history : list[str | int | bool | float] = []
    historyEnabled : bool = False

    failOverNum : int | float = -1
    failOverBool : bool = False

    throwExeption : bool = False

    def getInt(self, prompt : str, minimun : int = 0, maximun : int = 0) -> int:
        a = input(prompt)
        if self.history:
            self.history.append(a)
        try:
            if maximun == minimun: # This means there's no min or max
                return int(a)

            if int(a) > maximun:
                return self.failOverNum

            if int(a) < minimun:
                return self.failOverNum

            return int(a)
                    
        except:
            if self.throwExeption:
                raise "Wrong input type. Parse error."
            return self.failOverNum
        
    def getFloat(self, prompt : str) -> float:
        a = input(prompt)
        if self.history:
            self.history.append(a)
        try:
            return float(a)
        except:
            if self.throwExeption:
                raise "Wrong input type. Parse error."
            return self.failOverNum
        
    def getStr(self, prompt : str) -> str:
        a = input(prompt)
        if self.history:
            self.history.append(a)
        try:
            return float(a)
        except:
            if self.throwExeption:
                raise "Wrong input type. Parse error."
            return self.getNum

    def __init__(self, boolFailOver : bool, numFailOver : int | float, history : bool, raiseExeption : bool):
        self.failOverBool = boolFailOver
        self.failOverNum = numFailOver
        self.history = history
        self.throwExeption = raiseExeption
        
iHandler = InputHandler(False, -1, False, False)

libros = [
    "El quijote",
    "La odisea",
    "1984",
    "100 años de soledad"
]

librosPrestados = []

historial = []

def verCatalogo():
    print("Catalogo de libros:")
    for i, v in enumerate(libros):
        print(f"\t{i + 1}. {v}.")

def prestarLibro():
    print("Selecciona el libro que quieres pedir:")
    for i, v in enumerate(libros):
        print(f"\t{i + 1}. {v}.")

    userInput = iHandler.getInt("> Numero del libro:", 1, len(libros))

    if userInput == -1:
        print("Valor no valido, por favor ingresa un numero de libro valido.")
        return

    for libro in librosPrestados:
        if libros[userInput - 1] == libro:
            print("Ya tienes ese libro")
            return

    librosPrestados.append(libros[userInput - 1])
    historial.append(f"Prestado: {libros[userInput - 1]}")

def devolverLibro():
    print("Selecciona el libro que quieres devolver:")
    for i, v in enumerate(librosPrestados):
        print(f"\t{i + 1}. {v}.")
    
    if len(librosPrestados) == 0:
        print("No tienes ningun libro que devolver.")
        return

    userInput = iHandler.getInt("Selecciona el numero del libro que quieres devolver:", 1, len(librosPrestados))
    if userInput == -1:
        print("Valor no valido. Por favor ingresa el numero del libro que quieres devolver.")
        return
    
    try:
        lib = librosPrestados[userInput - 1]
        librosPrestados.remove(librosPrestados[userInput - 1])
        historial.append(f"Devuelto: {lib}")
    except:
        print("No tienes ese libro.")
        return

def verHistorial():
    print("Historial:")
    for historyItem in historial:
        print(f"\t{historyItem}.")

def salir():
    print("Fin del programa.")
    exit()

MenuOption("Ver catalogo", verCatalogo)
MenuOption("Pedir libro prestado", prestarLibro)
MenuOption("Devolver libro", devolverLibro)
MenuOption("Ver historial", verHistorial)
MenuOption("Salir", salir)

while True:
    print("Biblioteca:")
    for i, v in enumerate(menuOptions):
        print(f"\t{i + 1}. {v.name}.")

    userInput = iHandler.getInt("Selecciona una opcion:", 1, len(menuOptions))

    if userInput == -1:
        print("Opcion invalida, introduce el numero de la opcion que deseas realizar.")
        continue

    menuOptions[userInput - 1]()


