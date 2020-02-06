def compras():
    pass


def ventas():
    pass


def produccion():
    pass


def finanzas():
    pass


def clientes():
    pass


def almacen():
    pass


# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////// Login ///////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////
opciones = {"1": compras, "2": ventas, "3": produccion, "4": finanzas, "5": clientes,
            "6": almacen}

print("## LOGIN ##")
nombre = input("Usuario: ").strip()
contrasinal = input("Contraseña: ").strip()
nivelAcceso = -1

archivo = open("Usuarios.txt", "r")

for linea in archivo.readlines():
    login = linea.split(" ")

    if login[0] == nombre and login[1].split("\n")[0] == contrasinal:
        nivelAcceso = login[2]

print(nivelAcceso)

opcion = "0"
while opcion != "7":
    print('1.- Compras\n'
          '2.- Ventas\n'
          '3.- Producción\n'
          '4.- Finanzas\n'
          '5.- Clientes\n'
          '6.- Almacen\n'
          '7.- Salir')

    opcion = input("opcion: ")[0]

    if opcion != "7":
        opciones.get(opcion)()
