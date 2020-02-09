def compras():
    print("Compras")


def ventas():
    print("Ventas")


def produccion():
    print("Produccion")


def finanzas():
    print("Finanzas")


def clientes():
    print("Clientes")


def almacen():
    print("Almacen")


# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////// Login ///////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////
funciones = {"1": compras, "2": ventas, "3": produccion, "4": finanzas, "5": clientes,
             "6": almacen}

print("## LOGIN ##")
nombre = input("Usuario: ").strip()
contrasinal = input("Contraseña: ").strip()

archivo = open("Usuarios.txt", "r")

# ///////////////////////// Comprueba el nivel de acceso del usuario///////////////////
nivelAcceso = "denegado"

for linea in archivo.readlines():
    login = linea.split(" ")

    if login[0] == nombre and login[1].split("\n")[0] == contrasinal:
        nivelAcceso = login[2]
# ////////////////////////////////////////////////////////////////////////////////////

if nivelAcceso != "denegado":
    opcion = "0"

    niveles = {}

    opciones = {1: "1.- Compras",
                2: "2.- Ventas",
                3: "3.- Producción",
                4: "4.- Finanzas",
                5: "5.- Clientes",
                6: "6.- Almacen"}

    while opcion != "7":
        #si es mas de 1 es que existe ese numero en el archivo y añade al diccionario de niveles
        # esa opcion del menu
        for i in opciones:
            if nivelAcceso.count(str(i)) > 0: niveles[i] = opciones[i]
        #pinta el menu
        for nivel in niveles:
            print(niveles[nivel])

        print('7.- Salir')

        opcion = input("opcion: ")[0]

#////////////////////////////// Bloqueo de acceso denegado //////////////////////////////////////////////
        #aqui intenta acceder a la posicion del menu por si introduce una opcion que no puede acceder
        errores = False
        try:
            niveles[int(opcion)]
        except:
            errores = True
#////////////////////////////////////////////////////////////////////////////////////////////////////////

        if opcion != "7" and not errores:
            funciones.get(opcion)()
else:
    print("Usuario o contaseña incorrectos")
