
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
# /////////////////////////////////////////////////////////////////////////////////////
print("## LOGIN ##")
nombre = input("Usuario: ").strip()
contrasinal = input("Contraseña: ").strip()


archivo = open("Usuarios.txt", "r")
usuario = archivo.readline()
login = usuario.split(" ")

print(login[0])
print(login[1])
# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////// MENU ///////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////
opciones = {"1": compras, "2": ventas, "3": produccion, "4": finanzas, "5": clientes,
            "6": almacen}

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

    if opcion != "9":
        opciones.get(opcion)()
