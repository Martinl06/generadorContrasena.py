import secrets, string, sys

diccionario = {
  'letras': string.ascii_letters,
  'numeros': string.digits,
  'caracteres': string.punctuation
}

def contraseña_letras(longitud):
    contraseña_L = ''.join(secrets.choice(diccionario["letras"]) for _ in range(longitud))
    return contraseña_L

    
def contraseña_numeros(longitud):
    contraseña_N = ''.join(secrets.choice(diccionario["numeros"]) for _ in range(longitud))
    return contraseña_N

def contraseña_letras_numeros(longitud):
    contraseña_LN = ''.join(secrets.choice(diccionario["numeros"] + diccionario ["caracteres"]) for _ in range(longitud))
    return contraseña_LN


def contraseña_letras_numeros_caracteres(longitud):
    contraseña_LNC = ''.join(secrets.choice(diccionario["numeros"] + diccionario ["caracteres"] + diccionario["letras"]) for _ in range(longitud))
    return contraseña_LNC



def inicio():
    print("--------------------Welcome----------------------")
    print("Bienvenido al generador de contraseña v 0.1")
    print("--------------------|||||||----------------------")
    print("Seleccione una de las siguientes opciones: ")
    while True:
        print("1- Generar contraseñas solo de letras")
        print("2- Generar contraseñas solo de números")
        print("3- Generar contraseñas letras y números")
        print("4- Generar contraseñas Letras, números y caracteres")
        print("0- Salir")
        opcion = int(input("Seleccione: "))
        if opcion == 1:
            contraseña = contraseña_letras(10)
            print("Contraseña Generada: ", contraseña)
        elif opcion == 2:
            contraseña = contraseña_numeros(10)
            print("Contraseña Generada: ", contraseña)
        elif opcion == 3:
            contraseña = contraseña_letras_numeros(10)
            print("Contraseña Generada: ", contraseña)
        elif opcion == 4:
           contraseña = contraseña_letras_numeros_caracteres(10) 
           print("Contraseña Generada: ", contraseña)
        elif opcion == 0:
            print("Fin del programa")
            break
        else:
            print("Opcion inválida")               

inicio()