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

productos = [
    "Manzana",
    "Pan",
    "Leche"
]

cart = []

def mostrarProductos():
    print("Lista de productos disponibles:")
    for i, v in enumerate(productos):
        print(f"\t{i + 1}. {v}.")
    print("")

def verCarrito():
    print("Articulos del carrito:")
    for i, v in enumerate(cart):
        print(f"\t{i + 1}. {v}.")
    print("")

def agregarProducto():
    global cart

    mostrarProductos()

    userInput = iHandler.getInt("> Introduce numero del producto que quieres añadir al carrito:", 1, len(productos))

    if userInput == -1:
        print("Opcion no valida, por favor introduce un valor valido.")
        return

    cart.append(productos[userInput - 1])

    print(f"Se añadio {productos[userInput - 1]} al carrito.\n")

def showMenu():
    for i, v in enumerate(menuOptions):
        print(f"\t{i + 1}. {v.name}.")

def salir():
    print("Gracias, sus compras fueron :")
    for i, v in enumerate(cart):
        print(f"\t{i + 1}. {v}.")
    print("Fin del programa.")
    exit()

MenuOption("Ver productos", mostrarProductos)
MenuOption("Agregar productos", agregarProducto)
MenuOption("Ver carrito", verCarrito)
MenuOption("Salir", salir)

while True:
    print(" - - TIENDA - -")
    showMenu()
    userInput = iHandler.getInt("> Elige una opcion : ", 1, len(menuOptions))

    if userInput == -1:
        print("Opcion no valida, intenta de nuevo.")
        continue

    menuOptions[userInput - 1]()