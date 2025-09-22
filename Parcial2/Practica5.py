# leer menu, ordenar plato, cancelar pedido, ver cuenta, 

from modules.generic import MenuOption, InputHandler, menuOptions

platillos : dict[str:int] = {
    "Pizza": 120,
    "Hamburguesa" : 100,
    "Soda" : 30,
    "Burrito" : 30,
    "Desayuno" : 160,
    "Cafe" : 35
}

cuenta : list[str] = []

inputHdlr = InputHandler(False, -1, False, False) # Creo un objeto que me ayuda a procesar las entradas del usuario

def indexarPlatillo(g : int) -> str:
    for i, v in enumerate(platillos):
        if i == g:
            return v

def mostrarMenu():
    print("Menu:")
    for i, v in enumerate(platillos):
        print(f"\t{i+1}. {v}: ${platillos[v]}")
    print("\n")
    input("Presiona enter para continuar.")

def ordenarPlato():
    print("Ordenar:")
    for i, v in enumerate(platillos):
        print(f"\t{i+1}. {v}: ${platillos[v]}")
    userInput = inputHdlr.getInt(" > Introduce el numero del platillo que quieres pedir: ", 1, len(platillos))

    if userInput == -1:
        print("Ese no es un valor valido, por favor intenta de nuevo.")
        return
    
    pedido = indexarPlatillo(userInput - 1)

    cuenta.append(pedido)

    print(f"Pediste: {pedido} por el precio de ${platillos[pedido]}.\n")
    input("Presiona enter para continuar.")

def cancelarPedido():
    if len(cuenta) == 0:
        print("Haz pedido nada aun.")
        input("Presiona enter para continuar.")
        return
    print("Cancelar pedido:")
    for i, v in enumerate(cuenta):
        print(f"\t{i+1}. {v}.")
    
    userInput = inputHdlr.getInt(" > Selecciona el numero del pedido que deseas cancelar: ", 1, len(cuenta))
    if userInput == -1:
        print("Ese no es un valor valido, por favor intenta de nuevo.")
        return
    
    print(f"Se cancelo el platillo: {cuenta[userInput-1]}.")

    cuenta.pop(userInput-1)

    input("Presiona enter para continuar.")

def verCuenta():
    if len(cuenta) == 0:
        print("Haz pedido nada aun.")
        input("Presiona enter para continuar.")
        return
    print("Ver cuenta:")
    print("\tArticulo:\t\tCosto:")
    total = 0
    for i, v in enumerate(cuenta):
        print(f"\t{i+1}. {v} :\t\t${platillos[v]}")
        total += platillos[v]

    print(f"Total: {total}")

    input("Presiona enter para continuar.")

def salir():
    print("Fin del programa.")
    exit()

MenuOption("Mostrar menu", mostrarMenu)
MenuOption("Ordenar", ordenarPlato)
MenuOption("Cancelar orden", cancelarPedido)
MenuOption("Ver cuenta", verCuenta)
MenuOption("Salir", salir)

while True:
    print("Restaurant:")

    for i, v in enumerate(menuOptions):
        print(f"\t{i+1}. {v.name}.")

    userInput = inputHdlr.getInt(" > Introduce el numero de la accion quieres realizar: ", 1, len(menuOptions))

    if userInput == -1:
        print("Introduzca un valor valido:")
        continue

    menuOptions[userInput-1]()