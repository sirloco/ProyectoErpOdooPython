import Funcion

def editarOrden():
    print("editar orden de compra")

def anularOrden():
    print("anular orden de compra")

def mostrarOrdenes():
    print("mostrar ordenes de compra")

def ventas():
    print("Ventas")

def produccion():
    print("Produccion")

def finanzas():
    print("Finanzas")

def eliminaProducto():
    print("Elimina producto")

def muestraProducto():
    print("muestra producto")

def clientes():
    opcion = 0
    while opcion != 4:

        print("1.- Nuevo Cliente\n"
              "2.- Eliminar Cliente\n"
              "3.- Mostrar Clientes\n"
              "4.- Atras")

        opcion = input("opcion: ")[0]

        if opcion in fclientes.keys():
            fclientes.get(opcion)(False) if (opcion == "3") else fclientes.get(opcion)()


def compras():
    opcion = 0
    while opcion != "6":

        print("1. Crear orden de compra\n"
              "2. Editar orden de compra\n"
              "3. Anular orden de compra\n"
              "4. Crear proveedor\n"
              "5. Mostrar órdenes de compra\n"
              "6. Atras")

        opcion = input("opcion: ")[0]

        if opcion in fcompras.keys():
            fcompras.get(opcion)(False) if (opcion == "5") else fcompras.get(opcion)()

def almacen():
    opcion = 0
    while opcion != "4":

        print("1. Nuevo Producto\n"
              "2. Eliminar Producto\n"
              "3. Mostrar Productos\n"
              "4. Atras")

        opcion = input("opcion: ")[0]

        if opcion in falmacen.keys():
            falmacen.get(opcion)(False) if (opcion == "3") else falmacen.get(opcion)()

falmacen = {
    "1": Funcion.nuevoProducto,
    "2": Funcion.eliminaProducto,
    "3": Funcion.muestraProductos
}
fclientes = {
    "1": Funcion.nuevoCliente,
    "2": Funcion.eliminaCliente,
    "3": Funcion.muestraClientes
}
fcompras = {
    "1": Funcion.nuevaOrden,
    "2": editarOrden,
    "3": anularOrden,
    "4": Funcion.creaProveeodor,
    "5": Funcion.muestraOrdenesCompra
}

# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////// Login ///////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////
funciones = {
    "1": compras,
    "2": ventas,
    "3": produccion,
    "4": finanzas,
    "5": clientes,
    "6": almacen
}

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
        # si es mas de 1 es que existe ese numero en el archivo y añade al diccionario de niveles
        # esa opcion del menu
        for i in opciones:
            if nivelAcceso.count(str(i)) > 0: niveles[i] = opciones[i]
        # pinta el menu
        for nivel in niveles:
            print(niveles[nivel])

        print('7.- Salir')

        opcion = input("opcion: ")[0]

        # ////////////////////////////// Bloqueo de acceso denegado //////////////////////////////////////////////
        # aqui intenta acceder a la posicion del menu por si introduce una opcion que no puede acceder
        errores = False
        try:
            niveles[int(opcion)]
        except:
            errores = True
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////

        if opcion != "7" and not errores:
            funciones.get(opcion)()
else:
    print("Usuario o contaseña incorrectos")
