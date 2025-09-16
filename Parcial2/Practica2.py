# Maximo Jurado
# Practica 3
from typing import Callable, Any
import time

saldo = 1000
movementLog : list[str] = []

class MenuOption:
    name : str = "-def"
    method : Callable[[Any], Any] | None = lambda : print(f"Esta opcion no tiene un metodo definido.")
    
    def __init__(self, name : str , method : Callable[[Any], Any] | None = None):
        self.name = name
        self.method = method
        menuOptions.append(self)

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

def listOptions():
    """Solamente imprime las opciones en pantalla."""
    for i, opt in enumerate(menuOptions):
        print(f"\t{i+1}. {opt.name}.")

def getOption():
    """Ejecuta la opcion seleccionada"""
    print("Cajero automatico. Selecciona una opcion : ")
    listOptions()
    e = iHandler.getInt("Introduce el numero de la opcion que deseas realizar: ", 1, len(menuOptions)) # Esto no va a funcionar si solo hay una opcion 

    menuOptions[e-1].method()

def llog(text : str): # Funcion simple para logear los movimientos
    movementLog.append(text)

def menu_consultar():
    print(f" > Tienes ${saldo}.")
    llog(f"Se consulto el saldo. UNIX_TS: {time.time()}.")
    print("\n")

def menu_depositar():
    global saldo
    amnt = iHandler.getInt(" >> Introduce la cantidad que deseas depositar: ", 0, 5000)
    if amnt == iHandler.failOverNum:
        print(" > Ese valor no es valido.")
        return
    saldo += amnt
    print(f" > Depositaste ${amnt}, ahora tienes ${saldo}")
    llog(f"Se depositaron ${amnt}. UNIX_TS: {time.time()}.")
    print("\n")

def menu_retirar():
    global saldo
    amnt = iHandler.getInt(" >> Introduce la cantidad que deseas retirar: ", 0, 1000)
    if amnt == iHandler.failOverNum:
        print(" > Ese valor no es valido.")
        return
    saldo -= amnt
    if saldo < 0:
        saldo += amnt
        print(" > No tienes suficientes fondos.")
        return
    
    print(f" > Retiraste ${amnt}, ahora tienes ${saldo}")
    llog(f"Se depositaron ${amnt}. UNIX_TS: {time.time()}.")
    print("\n")

def menu_ver_movimientos():
    print("Historial de movimientos : ")
    for i, s in enumerate(movementLog):
        print(f"\t{i+1}. {s}")
    print("\n")

MenuOption("Consultar Saldo", menu_consultar)
MenuOption("Despositar", menu_depositar)
MenuOption("Retirar", menu_retirar)
MenuOption("Ver movimientos", menu_ver_movimientos)
MenuOption("Salir", lambda : exit(1))

while True:
    getOption()