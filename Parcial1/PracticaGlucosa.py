import re
print("Captura de datos :")
nss = input("\tNSS: ")
nombre = input("\tNombre: ")
apellidoPaterno = input("\tApellido paterno: ")
apellidoMaterno = input("\tApellido materno: ")
patologia = input("\tPalotologia: ")
temperatura = input("\tTemperatura: ")
medicion = input("\tMedicion de glucosa: ")

dia = ""
while True:
    diaInput = input("\tDia (ejemplo: 2015-04-1): ")
    dia = re.findall(r"(\d*)-(\d*)-(\d*)", diaInput)
    if not (dia[0][0] and dia[0][1]):
        input("\tFormato incorrecto, ingrese el valor de forma correcta: ")
    else:
        break

hora = ""
while True:
    horaInput = input("\tHora (ejemplo: 12:49): ")
    hora = re.findall(r"(\d*):(\d*)", horaInput)
    if not (hora[0][0] and hora[0][1]):
        input("\tFormato incorrecto, ingrese el valor de forma correcta: ")
    else:
        break



print("Datos capturados : ")
print("\tNSS: " + nss + " | Tipo : " + str(type(nss)))
print("\tNombre: " + nombre + " | Tipo : " + str(type(nombre)))
print("\tApellido Paterno: " + apellidoPaterno + " | Tipo : " + str(type(apellidoPaterno)))
print("\tApellido Materno: " + apellidoMaterno + " | Tipo : " + str(type(apellidoMaterno)))
print("\tTemperatura: " + temperatura + " | Tipo : " + str(type(patologia)))
print("\tMedicion de Glucosa: " + medicion + " | Tipo : " + str(type(medicion)))
print("\tDia de la medicion : " + dia[0][0] + "/" + dia[0][1] + "/" + dia[0][2] + " Hora: " + hora[0][0] + ":" + hora[0][1] + " | Tipo : " + str(type(dia[0])))