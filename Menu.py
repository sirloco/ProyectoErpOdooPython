import Funcion
import Vista
import BBDD

nombre = ""


def ventas():
    opcion = 0
    while opcion != "4":

        print("\n"
              "1. Crear Venta\n"
              "2. Anular orden Venta\n"
              "3. Mostrar Ventas\n"
              "4. Atras")

        opcion = input("opcion: ")[0]

        if opcion in fventas.keys():
            Funcion.log(nombre + " Accedió al Departamento de Ventas")
            fventas.get(opcion)(False) if (opcion == "3") else fventas.get(opcion)()


def empleados():
    opcion = 0
    while opcion != "4":

        print("\n"
              "1. Nuevo Empleado\n"
              "2. Eliminar Empleado\n"
              "3. Mostrar Empleados\n"
              "4. Atras")

        opcion = input("opcion: ")[0]

        if opcion in fempleados.keys():
            Funcion.log(nombre + " Accedió a gestión de empleados")
            fempleados.get(opcion)(False) if (opcion == "3") else fempleados.get(opcion)()


def clientes():
    opcion = 0
    while opcion != "4":

        print("\n"
              "1.- Nuevo Cliente\n"
              "2.- Eliminar Cliente\n"
              "3.- Mostrar Clientes\n"
              "4.- Atras")

        opcion = input("opcion: ")[0]

        if opcion in fclientes.keys():
            Funcion.log(nombre + " Accedió a Gestion de Clientes")
            fclientes.get(opcion)(False) if (opcion == "3") else fclientes.get(opcion)()


def compras():
    opcion = 0
    while opcion != "6":

        print("\n"
              "1. Crear orden de compra\n"
              "2. Anular orden de compra\n"
              "3. Crear proveedor\n"
              "4. Mostrar órdenes de compra\n"
              "5. imprimir orden de compra\n"
              "6. Atras")

        opcion = input("opcion: ")[0]

        if opcion in fcompras.keys():
            Funcion.log(nombre + " Accedió al Departamento de Compras")
            fcompras.get(opcion)(False) if (opcion == "4") else fcompras.get(opcion)()


def almacen():
    opcion = 0
    while opcion != "4":

        print("\n"
              "1. Nuevo Producto\n"
              "2. Eliminar Producto\n"
              "3. Mostrar Productos\n"
              "4. Atras")

        opcion = input("opcion: ")[0]

        if opcion in falmacen.keys():
            Funcion.log(nombre + " Accedió al Almacén")
            falmacen.get(opcion)(False) if (opcion == "3") else falmacen.get(opcion)()


falmacen = {
    "1": Vista.creaProducto,
    "2": Vista.eliminaProducto,
    "3": Vista.muestraProductos
}

fclientes = {
    "1": Vista.creaCliente,
    "2": Vista.eliminaCliente,
    "3": Vista.muestraClientes
}
fempleados = {
    "1": Vista.creaEmpleado,
    "2": Vista.eliminaEmpleado,
    "3": Vista.muestraEmpleados
}
fcompras = {
    "1": Vista.creaOrden,
    "2": Vista.anularOrden,
    "3": Vista.creaProveeodor,
    "4": Vista.muestraOrdenesCompra,
    "5": Vista.imprimirOrdenDeCompra
}
fventas = {
    "1": Vista.nuevaVenta,
    "2": Vista.anularVenta,
    "3": Vista.muestraVentas
}
funciones = {
    "1": compras,
    "2": ventas,
    "3": empleados,
    "4": clientes,
    "5": almacen
}

# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////// Login ///////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////
nivelAcceso = "denegado"

while nivelAcceso == "denegado":
    print("## LOGIN ##")
    nombre = input("Usuario: ").strip()
    contrasinal = input("Contraseña: ").strip()

    # ///////////////////////// Comprueba el nivel de acceso del usuario///////////////////
    db = BBDD.conectaBD()

    cursor = db.cursor()

    consulta = 'SELECT * FROM usuarios where nombre = "' + nombre + '" and pass = "' + contrasinal + '"'
    # Ejecutar SQL --> es un string
    cursor.execute(consulta)

    # Recoger más de un dato con fetchall()
    resultados = cursor.fetchone()

    if resultados is not None:
        nivelAcceso = resultados[2]  # el 2 corresponde con el campo 3 de la tabla de usuarios que es acceso

    # ////////////////////////////////////////////////////////////////////////////////////

    if nivelAcceso != "denegado":
        opcion = "0"

        niveles = {}

        opciones = {
            1: "1.- Compras",
            2: "2.- Ventas",
            3: "3.- Empleados",
            4: "4.- Clientes",
            5: "5.- Almacen"
        }

        while opcion != "6":
            # si es mas de 1 es que existe ese numero en el archivo y añade al diccionario de niveles
            # esa opcion del menu
            for i in opciones:
                if nivelAcceso.count(str(i)) > 0:
                    niveles[i] = opciones[i]
            # pinta el menu
            print("\n------------ MENU PRINCIPAL------------")
            for nivel in niveles:
                print(niveles[nivel])

            print('6.- Salir')
            print("---------------------------------------")
            opcion = input("opcion: ")[0]

            # ////////////////////////////// Bloqueo de acceso denegado //////////////////////////////////////////////
            # aqui intenta acceder a la posicion del menu por si introduce una opcion que no puede acceder
            errores = False
            try:
                niveles[int(opcion)]
            except:
                errores = True
            # ////////////////////////////////////////////////////////////////////////////////////////////////////////

            if opcion != "6" and not errores:
                funciones.get(opcion)()
    else:
        print("Usuario o contaseña incorrectos")
