import Clase
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

# lista de proveedores
proveedores = []
almacen = []
clientes = []
empleados = []
ordenesCompra = []
ordenesVenta = []


# ////////////////////////////////////////////////////////////////////////////////////
#                       MUESTRA LA LISTA DE PROVEEDORES
# ////////////////////////////////////////////////////////////////////////////////////
def muestraProveedor():
    log("Se ha Mostrado la lista de proveedores")
    repite = True if len(proveedores) > 0 else False
    while repite:
        i = 1
        for pro in proveedores:
            print(i, ": ", pro.getNombre())
            i += 1

        try:
            return int(input("Elige un proveedor o inserta 0 para crear uno nuevo: ")) - 1
        except:
            repite = True


# ////////////////////////////////////////////////////////////////////////////////////
#                       MUESTRA LA LISTA DE PRODUCTOS
# ////////////////////////////////////////////////////////////////////////////////////
def muestraProductos(quiereUnoConcreto):
    log("Se ha mostrardo la lista de productos")
    repite = True if len(almacen) > 0 else False
    while repite:
        i = 1
        for p in almacen:
            print(i, ": ", p.getNombre())
            i += 1

        if quiereUnoConcreto:
            try:
                return int(input("Elige un producto o inserta 0 para crear uno nuevo: ")) - 1
            except:
                repite = True
        else:
            repite = False


# ////////////////////////////////////////////////////////////////////////////////////
#                       MUESTRA LA LISTA DE CLIENTES
# ////////////////////////////////////////////////////////////////////////////////////
def muestraClientes(quiereUnoConcreto):
    log("Se ha mostrado la lista de clientes")
    repite = True if len(clientes) > 0 else False
    while repite:
        i = 1
        for c in clientes:
            print(i, ": ", c.getNombre())
            i += 1

        if quiereUnoConcreto:
            try:
                return int(input("Elige un cliente o pon un n para crear uno nuevo: ")) - 1
            except:
                repite = True
        else:
            repite = False


# ////////////////////////////////////////////////////////////////////////////////////
#                       MUESTRA LA LISTA DE CLIENTES
# ////////////////////////////////////////////////////////////////////////////////////
def muestraEmpleados(quiereUnoConcreto):
    log("Se ha mostrado la lista de empleados")
    repite = True if len(empleados) > 0 else False
    while repite:
        i = 1
        for e in empleados:
            print(i, ": ", e.getNombre())
            i += 1

        if quiereUnoConcreto:
            try:
                return int(input("Elige un empleado o pon un n para crear uno nuevo: ")) - 1
            except:
                repite = True
        else:
            repite = False


# ////////////////////////////////////////////////////////////////////////////////////
#                       MUESTRA LA LISTA DE ORDENES DE VENTA
# ////////////////////////////////////////////////////////////////////////////////////
def muestraVentas(quiereUnaConcreta):
    log("Se ha mostrado el listado de ordenes de venta")
    repite = True if len(ordenesVenta) > 0 else False
    while repite:
        i = 1
        for ov in ordenesVenta:

            for producto, cantidad in ov.getProductos().items():
                print(producto.getNombre(), ": ", cantidad)

            i += 1

        print("\n")

        if quiereUnaConcreta:
            try:
                return int(input("Elige una orden: ")) - 1
            except:
                repite = True
        else:
            repite = False


# ////////////////////////////////////////////////////////////////////////////////////
#                       MUESTRA LA LISTA DE ORDENES DE COMPRA
# ////////////////////////////////////////////////////////////////////////////////////
def muestraOrdenesCompra(quiereUnaConcreta):
    log("Se ha mostrado el listado de ordenes de compra")
    repite = True if len(ordenesCompra) > 0 else False
    while repite:
        i = 1
        for oc in ordenesCompra:
            print(i, ": Proveedor- >", oc.getProveedor().getNombre())

            for producto, cantidad in oc.getProductos().items():
                print(producto.getNombre(), ": ", cantidad)

            i += 1

        print("\n")

        if quiereUnaConcreta:
            try:
                return int(input("Elige una orden: ")) - 1
            except:
                repite = True
        else:
            repite = False


# ////////////////////////////////////////////////////////////////////////////////////
#                                  CREA ORDEN DE VENTA
# ////////////////////////////////////////////////////////////////////////////////////
def nuevaVenta():
    errores = False

    if not errores:
        listaProductos = {}

        clienteElegido = muestraClientes(True)

        if clienteElegido is None or clienteElegido < 0:
            print("-Creando nuevo Cliente-")
            nuevoCliente()
            clienteElegido = len(clientes) - 1

        repite = True
        while repite:
            productoElegido = muestraProductos(True)

            if productoElegido is None or productoElegido < 0:
                print("-Creando Nuevo Producto-")
                nuevoProducto()
                productoElegido = len(almacen) - 1

            cantidad = input("cantidad: ").strip()

            listaProductos[almacen[productoElegido]] = cantidad

            respuesta = input("¿Agregar otro producto? (s/n)").strip()

            repite = False if respuesta == "n" else True

        ordenVenta = Clase.OrdenVenta(listaProductos)
        ordenesVenta.append(ordenVenta)
        print("Orden Creada!\n")
        log("Se ha creado una orden de Venta")
    else:
        print(errores)


# ////////////////////////////////////////////////////////////////////////////////////
#                                  CREA ORDEN DE COMPRA
# ////////////////////////////////////////////////////////////////////////////////////
def nuevaOrden():
    errores = False

    if not errores:
        # Me interesa crear una lista de productos cada vez que se llame a esta funcion
        listaProductos = {}

        proveedorElegido = muestraProveedor()

        if proveedorElegido is None or proveedorElegido < 0:
            print("-Creando nuevo Proveedor-")
            creaProveeodor()
            proveedorElegido = len(proveedores) - 1

        repite = True
        while repite:
            productoElegido = muestraProductos(True)

            if productoElegido is None or productoElegido < 0:
                print("-Creando Nuevo Producto-")
                nuevoProducto()
                productoElegido = len(almacen) - 1

            cantidad = input("cantidad: ").strip()

            listaProductos[almacen[productoElegido]] = cantidad

            respuesta = input("¿Agregar otro producto? (s/n)").strip()

            repite = False if respuesta == "n" else True

        ordenCompra = Clase.OrdenCompra(proveedores[proveedorElegido], listaProductos)
        ordenesCompra.append(ordenCompra)
        print("Orden Creada!\n")
        log("Se ha creado una orden de compra")
        print("nueva orden de compra")
    else:
        print(errores)


# ////////////////////////////////////////////////////////////////////////////////////
#                            CREA PROVEEDOR NUEVO
# ////////////////////////////////////////////////////////////////////////////////////
def creaProveeodor():
    errores = False
    nombre = input("Nombre: ").strip()
    direccion = input("Direccion: ").strip()

    if nombre == "" or direccion == "": errores = "Error, campos obligatorios!"

    if not errores:

        proveedor = Clase.Persona(nombre, direccion)
        proveedores.append(proveedor)
        print("{0} Creado!\n".format(proveedor.getNombre()))
        log("Proveedor {0} Creado".format(proveedor.getNombre()))

    else:
        print(errores)


# ////////////////////////////////////////////////////////////////////////////////////
#                            CREA EMPLEADO NUEVO
# ////////////////////////////////////////////////////////////////////////////////////
def nuevoEmpleado():
    errores = False
    nombre = input("Nombre: ").strip()
    direccion = input("Direccion: ").strip()

    if nombre == "" or direccion == "": errores = "Error, campos obligatorios!"

    if not errores:

        empleado = Clase.Persona(nombre, direccion)
        empleados.append(empleado)
        print("{0} Creado!\n".format(empleado.getNombre()))
        log("Empleado {0} Creado".format(empleado.getNombre()))

    else:
        print(errores)


# ////////////////////////////////////////////////////////////////////////////////////
#                           CREA PRODUCTO NUEVO
# ////////////////////////////////////////////////////////////////////////////////////
def nuevoProducto():
    errores = False
    nombre = input("Nombre: ").strip()
    precio = input("Precio: ").strip()

    if nombre == "" or precio == "": errores = "Error, campos obligatorios!"

    if not errores:

        producto = Clase.Producto(nombre, precio)
        almacen.append(producto)
        print("{0} Creado!\n".format(producto.getNombre()))
        log("Producto {0} Creado".format(producto.getNombre()))
    else:
        print(errores)


# ////////////////////////////////////////////////////////////////////////////////////
#                           CREA CLIENTE NUEVO
# ////////////////////////////////////////////////////////////////////////////////////
def nuevoCliente():
    errores = False
    nombre = input("Nombre: ").strip()
    direccion = input("Direccion: ").strip()

    if nombre == "" or direccion == "": errores = "Error, campos obligatorios!"

    if not errores:
        cliente = Clase.Producto(nombre, direccion)
        clientes.append(cliente)
        print("{0} Creado!\n".format(cliente.getNombre()))
        log("Cliente {0} Creado".format(cliente.getNombre()))
    else:
        print(errores)


# ////////////////////////////////////////////////////////////////////////////////////
#                           ELIMINAR PRODUCTO
# ////////////////////////////////////////////////////////////////////////////////////
def eliminaProducto():
    eligeUno = True
    productoElegido = muestraProductos(eligeUno)

    if productoElegido is None:
        print("Nada que borrar\n")
    else:
        product = almacen.pop(productoElegido).getNombre()
        print(product + " Eliminado\n")
        log("Producto " + product + " Eliminado")


# ////////////////////////////////////////////////////////////////////////////////////
#                           ELIMINAR CLIENTE
# ////////////////////////////////////////////////////////////////////////////////////
def eliminaCliente():
    eligeUno = True
    clienteElegido = muestraClientes(eligeUno)

    if clienteElegido is None:
        print("Nada que borrar\n")
    else:
        cli = clientes.pop(clienteElegido).getNombre()
        print(cli + " Eliminado\n")
        log("Cliente " + cli + " Eliminado")


# ////////////////////////////////////////////////////////////////////////////////////
#                           ELIMINAR EMPLEADO
# ////////////////////////////////////////////////////////////////////////////////////
def eliminaEmpleado():
    eligeUno = True
    empleadoElegido = muestraEmpleados(eligeUno)

    if empleadoElegido is None:
        print("Nada que borrar\n")
    else:
        empl = clientes.pop(empleadoElegido).getNombre()
        print(empl + " Eliminado\n")
        log("Empleado " + empl + " Eliminado")


# ////////////////////////////////////////////////////////////////////////////////////
#                           ELIMINAR ORDEN DE COMPRA
# ////////////////////////////////////////////////////////////////////////////////////
def anularOrden():
    eligeUno = True
    ordenElegida = muestraOrdenesCompra(eligeUno)

    if ordenElegida is None:
        print("Nada que borrar\n")
    else:
        ordenesCompra.pop(ordenElegida)
        print("Eliminada!\n")
        log("Anulada orden de compra")


# ////////////////////////////////////////////////////////////////////////////////////
#                           ELIMINAR ORDEN DE COMPRA
# ////////////////////////////////////////////////////////////////////////////////////
def anularVenta():
    eligeUno = True
    ordenElegida = muestraVentas(eligeUno)

    if ordenElegida is None:
        print("Nada que borrar\n")
    else:
        ordenesVenta.pop(ordenElegida)
        print("Eliminada!\n")
        log("Anulada orden de venta")


# ////////////////////////////////////////////////////////////////////////////////////
#                           REGISTRO DE LOG
# ////////////////////////////////////////////////////////////////////////////////////
def log(reg):
    archivo = open("log.txt", "a")

    ahora = datetime.now()

    archivo.writelines(
        (reg + " el " + ahora.strftime("%d-%m-%Y  %H:%M:%S") + "\n"))

    archivo.close()

# ////////////////////////////////////////////////////////////////////////////////////
#                       MUESTRA LA LISTA DE ORDENES DE COMPRA
# ////////////////////////////////////////////////////////////////////////////////////
def imprimirOrdenDeCompra():
    ordenElegida = muestraOrdenesCompra(True)
    w, h = A4
    c = canvas.Canvas("Orden_de_Compra.pdf")
    # Rectángulo.
    c.drawString(50, h - 50, ordenesCompra[ordenElegida].getProveedor().getNombre())
    columna = 75
    linea = 65

    for producto, cantidad in ordenesCompra[ordenElegida].getProductos().items():
        c.drawString(columna, h - linea, producto.getNombre() + ": " + cantidad)
        linea += 25

    c.showPage()
    c.save()
    print("Documento Impreso revisa la carpeta del proyecto")