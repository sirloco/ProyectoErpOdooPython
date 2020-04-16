import time

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

import Funcion

"""
////////////////////////////////////////////////////////////////////////////////////
                           CREA PRODUCTO NUEVO
////////////////////////////////////////////////////////////////////////////////////
"""


def creaProducto():
    repite = True

    while repite:
        errores = False

        nombre = input("Nombre: ").strip()
        precio = input("Precio: ").strip()
        cantidad = input("Cantidad ").strip()

        if nombre == "" or precio == "" or cantidad == "":
            errores = "Campos obligatorios!"

        if not errores:
            producto = Funcion.nuevoProducto(nombre, precio, cantidad)
            print("No se pudo crear " + nombre if not producto else "Producto {0} Creado!".format(nombre))
            repite = errores
        else:
            print(errores)


"""
////////////////////////////////////////////////////////////////////////////////////
                           CREA CLIENTE NUEVO
////////////////////////////////////////////////////////////////////////////////////
"""


def creaCliente():
    repite = True

    while repite:
        errores = False

        nombre = input("Nombre: ").strip()
        direccion = input("Direccion: ").strip()

        if nombre == "" or direccion == "":
            errores = "Error, campos obligatorios!"

        if not errores:
            cliente = Funcion.nuevoCliente(nombre, direccion)
            print("No se pudo crear " + nombre if not cliente else "Cliente {0} Creado!".format(nombre))
            repite = errores
        else:
            print(errores)


"""
////////////////////////////////////////////////////////////////////////////////////
                            CREA EMPLEADO NUEVO
////////////////////////////////////////////////////////////////////////////////////
"""


def creaEmpleado():
    repite = True

    while repite:
        errores = False

        nombre = input("Nombre: ").strip()
        direccion = input("Direccion: ").strip()

        if nombre == "" or direccion == "":
            errores = "Error, campos obligatorios!"

        if not errores:
            empleado = Funcion.nuevoEmpleado(nombre, direccion)
            print("No se pudo crear " + nombre if not empleado else "Empleado {0} Creado!".format(nombre))
            repite = errores
        else:
            print(errores)


"""
////////////////////////////////////////////////////////////////////////////////////
                            CREA PROVEEDOR NUEVO
////////////////////////////////////////////////////////////////////////////////////
"""


def creaProveeodor():
    repite = True

    while repite:
        errores = False

        nombre = input("Nombre: ").strip()
        direccion = input("Direccion: ").strip()

        if nombre == "" or direccion == "":
            errores = "Error, campos obligatorios!"

        if not errores:
            proveedor = Funcion.nuevoProveeodor(nombre, direccion)
            print("No se pudo crear " + nombre if not proveedor else "Proveedor {0} Creado!".format(nombre))
            repite = errores
        else:
            print(errores)


"""
////////////////////////////////////////////////////////////////////////////////////
                       MUESTRA LA LISTA DE PRODUCTOS
////////////////////////////////////////////////////////////////////////////////////
"""


def muestraProductos(quiereUnoConcreto):
    productos = Funcion.montaProductos()

    repite = True if len(productos) > 0 else False  # si está vacia la lista no muestra nada

    while repite:
        print("\nid   Nombre       Precio    Cantidad")
        print("--------------------------------------")
        for id, producto in productos.items():
            if producto.getVisibilidad() == 1:
                print("{0:<4} {1:<12} {2:<12} {3}".format(id + 1, producto.getNombre(), producto.getPrecio(),
                                                          producto.getCantidad()))

        if quiereUnoConcreto:
            try:  # devuelvo el id elegido si no existe vuelve a pedir
                id = int(input("Elige un id producto: ")) - 1
                if productos[id].getVisibilidad() == 0:
                    id = None
                return productos[id]
            except:
                print("Elige un producto de la lista!")
                repite = True
        else:
            repite = False


"""
////////////////////////////////////////////////////////////////////////////////////
                       MUESTRA LA LISTA DE PROVEEDORES 
////////////////////////////////////////////////////////////////////////////////////
"""


def muestraProveedor():
    proveedores = Funcion.montaProveedores()

    repite = True if len(proveedores) > 0 else False

    while repite:
        print("\nid   Nombre")
        print("-----------")

        for id, proveedor in proveedores.items():
            print(id + 1, ": ", proveedor.nombre())

        try:  # Con el id que elige el usuario obtengo la posicion del objeto y devuelvo el objeto
            opcion = input("Elige un id proveedor o 's' para salir: ")

            if opcion.lower() == 's':
                break
            return proveedores[int(opcion) - 1]
        except:
            repite = True


"""
////////////////////////////////////////////////////////////////////////////////////
                       MUESTRA LA LISTA DE EMPLEADOS
////////////////////////////////////////////////////////////////////////////////////
"""


def muestraEmpleados(quiereUnoConcreto):
    empleados = Funcion.montaEmpleados()

    repite = True if len(empleados) > 0 else False

    while repite:
        print("\nid   Nombre")
        print("-----------")

        for id, empleado in empleados.items():
            print(id + 1, ": ", empleado.nombre())

        if quiereUnoConcreto:
            try:  # Con el id que elige el usuario obtengo la posicion del objeto y devuelvo el objeto
                return empleados[int(input("Elige un id empleado o 'n' para crear uno nuevo: ")) - 1]
            except:
                repite = True
        else:
            repite = False


"""
////////////////////////////////////////////////////////////////////////////////////
                       MUESTRA LA LISTA DE CLIENTES
////////////////////////////////////////////////////////////////////////////////////
"""


def muestraClientes(quiereUnoConcreto):
    clientes = Funcion.montaClientes()

    repite = True if len(clientes) > 0 else False

    while repite:
        print("\nid   Nombre")
        print("-----------")

        for id, cliente in clientes.items():
            print(id + 1, ": ", cliente.nombre())

        if quiereUnoConcreto:
            try:  # Con el id que elige el usuario obtengo la posicion del objeto y devuelvo el objeto
                return clientes[int(input("Elige un id cliente o pon 'n' para crear uno nuevo: ")) - 1]
            except:
                repite = True
        else:
            repite = False


"""
////////////////////////////////////////////////////////////////////////////////////
                           ELIMINAR PRODUCTO
////////////////////////////////////////////////////////////////////////////////////
"""


def eliminaProducto():
    productoElegido = muestraProductos(True)  # True porque nos interesa que devuelva un objeto producto concreto
    if not productoElegido:
        print("Nada que borrar")
    elif Funcion.quitaProducto(productoElegido):
        print(productoElegido.getNombre() + " Eliminado!")
        muestraProductos(False)
    else:
        print("Error al eliminar " + productoElegido.getNombre())


"""
////////////////////////////////////////////////////////////////////////////////////
                           ELIMINAR CLIENTE
 ////////////////////////////////////////////////////////////////////////////////////
"""


def eliminaCliente():
    clienteElegido = muestraClientes(True)  # True porque nos interesa que devuelva un objeto producto concreto

    if clienteElegido is None:
        print("Nada que borrar\n")
    elif Funcion.quitaCliente(clienteElegido):
        print(clienteElegido.getNombre() + " Eliminado!")
    else:
        print("Error al eliminar " + clienteElegido.getNombre())


"""
////////////////////////////////////////////////////////////////////////////////////
                           ELIMINAR EMPLEADO
 ////////////////////////////////////////////////////////////////////////////////////
"""


def eliminaEmpleado():
    empleadoElegido = muestraEmpleados(True)  # True porque nos interesa que devuelva un objeto producto concreto

    if empleadoElegido is None:
        print("Nada que borrar\n")
    elif Funcion.quitaEmpleado(empleadoElegido):
        print(empleadoElegido.getNombre() + " Eliminado!")
    else:
        print("Error al eliminar " + empleadoElegido.getNombre())


"""
////////////////////////////////////////////////////////////////////////////////////
                           CREA ORDEN COMPRA NUEVA
////////////////////////////////////////////////////////////////////////////////////
"""


def creaOrden():
    errores = False

    if not errores:
        # Me interesa crear una lista de productos cada vez que se llame a esta funcion será la que contenga el objeto
        listaProductos = []

        proveedorElegido = muestraProveedor()

        if proveedorElegido:

            repite = True
            while repite:
                productoElegido = muestraProductos(True)

                if productoElegido is None:
                    print("-Creando Nuevo Producto-")
                    creaProducto()
                    productoElegido = muestraProductos(True)

                cantidad = input("Cuantos quieres: ").strip()

                productoElegido.setCantidad(cantidad)

                listaProductos.append(productoElegido)

                respuesta = input("¿Agregar otro producto? (s/n)").strip()

                repite = False if respuesta == "n" else True

            Funcion.nuevaOrdenCompra(proveedorElegido, listaProductos)

            print("Orden Creada!")
            print("nueva orden de compra")
    else:
        print(errores)


"""
////////////////////////////////////////////////////////////////////////////////////
                                  CREA ORDEN DE VENTA
////////////////////////////////////////////////////////////////////////////////////
"""


def nuevaVenta():
    errores = False

    if not errores:
        listaProductos = []

        clienteElegido = muestraClientes(True)

        if clienteElegido:

            repite = True
            while repite:
                productoElegido = muestraProductos(True)

                if productoElegido is None:
                    print("-Creando Nuevo Producto-")
                    creaProducto()
                    productoElegido = muestraProductos(True)

                cantidad = input("cantidad: ").strip()

                productoElegido.setCantidad(cantidad)

                listaProductos.append(productoElegido)

                respuesta = input("¿Agregar otro producto? (s/n)").strip()

                repite = False if respuesta == "n" else True

            Funcion.nuevaOrdenVenta(clienteElegido, listaProductos)
            print("Orden Creada!")
        else:
            print(errores)


"""
////////////////////////////////////////////////////////////////////////////////////
                       MUESTRA LA LISTA DE ORDENES DE VENTA
////////////////////////////////////////////////////////////////////////////////////
"""


def muestraVentas(quiereUnaConcreta):
    ordenesVenta = Funcion.montaOrdenesVenta()

    repite = True if len(ordenesVenta) > 0 else False

    while repite:
        for id, ov in ordenesVenta.items():
            total = 0

            print("id:" + str(id + 1) + " Nº Albaran: " + str(ov.getAlbaran()),
                  " Cliente: " + str(ov.getCliente().getNombre()))
            print("Producto   cantidad   precio")
            print("------------------------------")

            for producto in ov.getProductos():
                print(
                    "{0:<12} {1:>4} {2:>11}".format(producto.getNombre(), producto.getCantidad(), producto.getPrecio()))
                total += producto.getPrecio() * producto.getCantidad()

            print("______________________________")
            print("Total: {0:>22}\n\n".format(total))

        if quiereUnaConcreta:
            try:
                return ordenesVenta[int(input("Elige un id orden de venta: ")) - 1]
            except:
                repite = True
        else:
            repite = False


"""
////////////////////////////////////////////////////////////////////////////////////
                       MUESTRA LA LISTA DE ORDENES DE COMPRA
////////////////////////////////////////////////////////////////////////////////////
"""


def muestraOrdenesCompra(quiereUnaConcreta):
    ordenesCompra = Funcion.montaOrdenesCompra()

    repite = True if len(ordenesCompra) > 0 else False
    while repite:
        for id, oc in ordenesCompra.items():
            total = 0

            print("id:" + str(id + 1) + " Nº Albaran: " + str(oc.getAlbaran()),
                  " Proveedor: " + str(oc.getProveedor().getNombre()))
            print("Producto   cantidad   precio")
            print("------------------------------")
            for producto in oc.getProductos():
                print(
                    "{0:<12} {1:>4} {2:>11}".format(producto.getNombre(), producto.getCantidad(), producto.getPrecio()))
                total += producto.getPrecio() * producto.getCantidad()

            print("______________________________")
            print("Total: {0:>22}\n\n".format(total))

        if quiereUnaConcreta:
            try:
                return ordenesCompra[int(input("Elige un id orden de compra: ")) - 1]
            except:
                repite = True
        else:
            repite = False


"""
////////////////////////////////////////////////////////////////////////////////////
                           ELIMINAR ORDEN DE COMPRA
////////////////////////////////////////////////////////////////////////////////////
"""


def anularOrden():
    ordenElegida = muestraOrdenesCompra(True)

    if ordenElegida is None:
        print("Nada que borrar")
    elif Funcion.quitaOrdenCompra(ordenElegida):
        print("Albaran " + ordenElegida.getAlbaran() + " Eliminado!")
    else:
        print("Error al eliminar el albaran: " + ordenElegida.getAlbaran())


"""
////////////////////////////////////////////////////////////////////////////////////
                           ELIMINAR ORDEN DE VENTA
////////////////////////////////////////////////////////////////////////////////////
"""


def anularVenta():
    ordenElegida = muestraVentas(True)

    if ordenElegida is None:
        print("Nada que borrar")
    elif Funcion.quitaOrdenVenta(ordenElegida):
        print("Albaran " + ordenElegida.getAlbaran() + " Eliminado!")
    else:
        print("Error al eliminar el albaran: " + ordenElegida.getAlbaran())


"""
////////////////////////////////////////////////////////////////////////////////////
                       MUESTRA LA LISTA DE ORDENES DE COMPRA PDF
////////////////////////////////////////////////////////////////////////////////////
"""


def imprimirOrdenDeCompra():
    ordenElegida = muestraOrdenesCompra(True)

    doc = SimpleDocTemplate("Compra {0}.pdf".format(ordenElegida.getAlbaran()), pagesize=A4,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)

    justificado = ParagraphStyle(name='Justify', alignment=TA_JUSTIFY)
    derecha = ParagraphStyle(name='derecha', alignment=TA_RIGHT)
    izquierda = ParagraphStyle('parrafos', alignment=TA_LEFT, fontSize=12)

    Story = []
    total = 0

    styles = getSampleStyleSheet()

    logo = "logo.jpg"
    im = Image(logo, 3.5 * cm, 2 * cm)
    im.hAlign = 'RIGHT'
    Story.append(im)

    Story.append(Spacer(1, 48))

    texto = '<font size="17">Albaran: {0}</font>'.format(ordenElegida.getAlbaran())
    Story.append(Paragraph(texto, styles["Normal"]))

    Story.append(Spacer(1, 12))

    proveedor = Paragraph(u"Proveedor: " + ordenElegida.getProveedor().getNombre(), izquierda)
    fecha = Paragraph(u"Fecha: " + time.strftime('%d/%m/%Y'), izquierda)
    datos = [[proveedor, fecha]]
    cabecera = Table(datos, colWidths=[11.5 * cm, 4 * cm])
    estiloTabla = [('BOX', (0, 0), (-1, -1), 0.25, colors.black)]
    cabecera.setStyle(estiloTabla)
    Story.append(cabecera)
    datos.clear()

    datos = [["Nombre", "Cantidad", "Precio"]]
    titulo = Table(datos, colWidths=[10 * cm, 4 * cm, 1.5 * cm])
    estiloTabla = [('BOX', (0, 0), (-1, -1), 0.25, colors.black)]
    titulo.setStyle(estiloTabla)
    Story.append(titulo)

    datos.clear()
    i = 0
    for producto in ordenElegida.getProductos():
        fila = producto.getNombre(), producto.getCantidad(), producto.getPrecio()
        datos.append(fila)
        total += producto.getPrecio() * producto.getCantidad()
        if not i % 2:
            estiloTabla.append(("BACKGROUND", (0, i), (-1, i), colors.lightgrey))
        i += 1

    tabla_datos = Table(datos, colWidths=[10 * cm, 4 * cm, 1.5 * cm], style=TableStyle(estiloTabla))

    estiloTabla = [('BOX', (0, 0), (-1, -1), 0.25, colors.black)]
    tabla_datos.setStyle(estiloTabla)

    Story.append(tabla_datos)

    Story.append(Spacer(1, 12))

    texto = 'Total: {0} €'.format(total)
    Story.append(Paragraph(texto, derecha))

    Story.append(Spacer(1, 12))

    doc.build(Story)

    print("Documento Impreso revisa la carpeta del proyecto")
