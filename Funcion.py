import Clase
from datetime import datetime
import BBDD

# listas
proveedores = {}
almacen = {}
clientes = {}
empleados = {}
ordenesCompra = {}
ordenesVenta = {}

"""
////////////////////////////////////////////////////////////////////////////////////
                            CREA VENTA NUEVA
////////////////////////////////////////////////////////////////////////////////////
"""


def nuevaOrdenVenta(cliente, productos):
    dateTimeObj = datetime.now()
    albaran = dateTimeObj.strftime(str(cliente.getId()) + "%d%m%Y%H%M%S")
    ordenVenta = Clase.OrdenVenta(cliente, productos, albaran)
    if BBDD.guardaOrdenVenta(ordenVenta):
        montaOrdenesVenta()
        log("Venta {0} Creada".format(albaran))
        return ordenVenta


"""
////////////////////////////////////////////////////////////////////////////////////
                            CREA ORDEN COMPRA NUEVA
////////////////////////////////////////////////////////////////////////////////////
"""


def nuevaOrdenCompra(proveedor, productos):
    dateTimeObj = datetime.now()
    albaran = dateTimeObj.strftime(str(proveedor.getId()) + "%d%m%Y%H%M%S")
    ordenCompra = Clase.OrdenCompra(proveedor, productos, albaran)

    if BBDD.guardaOrdenCompra(ordenCompra):
        montaOrdenesCompra()
        log("Orden de compra {0} Creada".format(albaran))
        return ordenCompra


"""
////////////////////////////////////////////////////////////////////////////////////
                            CREA PROVEEDOR NUEVO
////////////////////////////////////////////////////////////////////////////////////
"""


def nuevoProveeodor(nombre, direccion):
    proveedor = Clase.Proveedor(nombre, direccion)

    if BBDD.guardaPersona(proveedor):
        montaProveedores()
        log("Proveedor {0} Creado".format(nombre))
        return proveedor


"""
////////////////////////////////////////////////////////////////////////////////////
                            CREA EMPLEADO NUEVO
////////////////////////////////////////////////////////////////////////////////////
"""


def nuevoEmpleado(nombre, direccion):
    empleado = Clase.Empleado(nombre, direccion)

    if BBDD.guardaPersona(empleado):
        montaEmpleados()
        log("Empleado {0} Creado".format(nombre))
        return empleado


"""
////////////////////////////////////////////////////////////////////////////////////
                           CREA CLIENTE NUEVO
////////////////////////////////////////////////////////////////////////////////////
"""


def nuevoCliente(nombre, direccion):
    cliente = Clase.Cliente(nombre, direccion)

    if BBDD.guardaPersona(cliente):
        montaClientes()
        log("Cliente {0} Creado".format(nombre))
        return cliente


"""
////////////////////////////////////////////////////////////////////////////////////
                           CREA PRODUCTO NUEVO
////////////////////////////////////////////////////////////////////////////////////
"""


def nuevoProducto(nombre, precio, cantidad):
    producto = Clase.Producto(nombre, precio, cantidad)

    if BBDD.guardaProducto(producto):
        montaProductos()
        log("Producto {0} Creado".format(producto.getNombre()))
        return producto


"""
////////////////////////////////////////////////////////////////////////////////////
                           ELIMINAR PRODUCTO
////////////////////////////////////////////////////////////////////////////////////
"""


def quitaProducto(productoElegido):
    resultado = BBDD.bajaProducto(productoElegido.getId())

    if resultado:  # Elimina de la BD el producto y devuelve true
        del almacen[productoElegido.getId()]  # Elimina del diccionario el producto tb
        log(productoElegido.getNombre() + " Eliminado")

    return resultado


"""
////////////////////////////////////////////////////////////////////////////////////
                           ELIMINAR CLIENTE
 ////////////////////////////////////////////////////////////////////////////////////
"""


def quitaCliente(clienteElegido):
    resultado = BBDD.bajaPersona(clienteElegido.getId())  # Elimina de la BD el cliente y devuelve true

    if resultado:
        del clientes[clienteElegido.getId()]  # Elimina de la lista el cliente tb
        log("Cliente " + clienteElegido.getNombre() + " Eliminado")

    return resultado


"""
////////////////////////////////////////////////////////////////////////////////////
                           ELIMINAR EMPLEADO
////////////////////////////////////////////////////////////////////////////////////
"""


def quitaEmpleado(empleadoElegido):
    resultado = BBDD.bajaPersona(empleadoElegido.getId())  # Elimina de la BD el empleado y devuelve true

    if resultado:
        del empleados[empleadoElegido.getId()]  # Elimina de la lista el empleado tb
        log("Empleado " + empleadoElegido.getNombre() + " Eliminado")

    return resultado


"""
////////////////////////////////////////////////////////////////////////////////////
                           ELIMINAR ORDEN COMPRA
////////////////////////////////////////////////////////////////////////////////////
"""


def quitaOrdenCompra(ordenElegida):
    resultado = BBDD.bajaOrdenCompra(ordenElegida.getAlbaran())  # Elimina de la BD la orden de compra y devuelve true

    if resultado:
        del ordenesCompra[ordenElegida.getId()]  # Elimina de la lista la compra tb
        log("Albaran: " + ordenElegida.getAlbaran() + " Eliminado")

    return resultado


"""
////////////////////////////////////////////////////////////////////////////////////
                           ELIMINAR ORDEN VENTA
////////////////////////////////////////////////////////////////////////////////////
"""


def quitaOrdenVenta(ordenElegida):
    resultado = BBDD.bajaOrdenVenta(ordenElegida.getAlbaran())  # Elimina de la BD la venta y devuelve true

    if resultado:
        del ordenesVenta[ordenElegida.getId()]  # Elimina de la lista la venta tb
        log("Albaran: " + ordenElegida.getAlbaran() + " Eliminado")

    return resultado


"""
////////////////////////////////////////////////////////////////////////////////////
                           REGISTRO DE LOG
////////////////////////////////////////////////////////////////////////////////////
"""


def log(reg):
    archivo = open("log.txt", "a")

    ahora = datetime.now()

    archivo.writelines(
        (reg + " el " + ahora.strftime("%d-%m-%Y  %H:%M:%S") + "\n"))

    archivo.close()


"""
////////////////////////////////////////////////////////////////////////////////////
                 CREA OBJETOS DE TIPO EMPLEADO CON LA LISTA RECIBIDA
////////////////////////////////////////////////////////////////////////////////////
"""


def montaEmpleados():
    listaEmpleados = BBDD.listadoPersonas(BBDD.EMPLEADO)
    empleados.clear()
    if listaEmpleados:
        for emp in listaEmpleados:
            empleado = Clase.Empleado(emp[1], emp[2])
            empleado.setId(emp[0])
            empleados[emp[0]] = empleado

        log("Se ha mostrado la lista de empleados")

    return empleados


"""
////////////////////////////////////////////////////////////////////////////////////
                       CREA OBJETOS DE TIPO CLIENTES CON LA LISTA RECIBIDA
////////////////////////////////////////////////////////////////////////////////////
"""


def montaClientes():
    listaClientes = BBDD.listadoPersonas(BBDD.CLIENTE)
    clientes.clear()
    if listaClientes:
        for cli in listaClientes:
            cliente = Clase.Cliente(cli[1], cli[2])
            cliente.setId(cli[0])
            clientes[cli[0]] = cliente

        log("Se ha mostrado la lista de clientes")

    return clientes


"""
////////////////////////////////////////////////////////////////////////////////////
                    CREA OBJETOS DE TIPO PROVEEDOR CON LA LISTA RECIBIDA
////////////////////////////////////////////////////////////////////////////////////
"""


def montaProveedores():
    listaProveedores = BBDD.listadoPersonas(BBDD.PROVEEDOR)
    proveedores.clear()
    if listaProveedores:
        for pro in listaProveedores:
            proveedor = Clase.Proveedor(pro[1], pro[2])
            proveedor.setId(pro[0])
            proveedores[pro[0]] = proveedor

        log("Se ha mostrado la lista de Proveedores")

    return proveedores


"""
////////////////////////////////////////////////////////////////////////////////////
                    CREA OBJETOS DE TIPO PRODUCTO CON LA LISTA RECIBIDA
////////////////////////////////////////////////////////////////////////////////////
"""


def montaProductos():
    listaProductos = BBDD.listadoProductos()
    almacen.clear()
    if listaProductos:
        for pro in listaProductos:
            producto = Clase.Producto(pro[1], pro[2], pro[3])  # el 1 y el 2 son las columnas de nombre y direccion
            producto.setId(pro[0])
            producto.setVisibilidad(pro[4])
            almacen[pro[0]] = producto

        log("Se ha mostrardo la lista de productos")

    return almacen


"""
////////////////////////////////////////////////////////////////////////////////////
                    CREA OBJETOS DE TIPO ORDEN COMPRA CON LA LISTA RECIBIDA
////////////////////////////////////////////////////////////////////////////////////
"""


def montaOrdenesCompra():
    listaProductosAlbaran = []
    listaOrdenesCompra = BBDD.listadoOrdenesCompra()
    montaProductos()
    montaProveedores()
    ordenesCompra.clear()
    if listaOrdenesCompra:

        albaran = 0
        proveedor = 0
        linea = 0

        for oc in listaOrdenesCompra:  # Recorre todas las filas de la tabla odenes compra

            # si no coincide el albaran con el anterior y no es la primera linea  o si es el ultimo crea orden de compra
            if albaran != oc[1] and linea > 0 or linea == len(listaOrdenesCompra) - 1:
                if linea == len(listaOrdenesCompra) - 1:
                    listaProductosAlbaran.append(almacen[oc[3]])  # se añade el producto a la lista
                # si ha cambiado de compra  se crea la compra
                lista = listaProductosAlbaran.copy()  # se hace una copia porque si no al borrar borra la referencia
                ordenCompra = Clase.OrdenCompra(proveedores[proveedor], lista, albaran)
                ordenCompra.setId(oc[0])
                ordenesCompra[oc[0]] = ordenCompra  # se guarda en la lista de ordenes de compra con su id
                listaProductosAlbaran.clear()  # se vacia la lista de productos para la siguiente compra

            listaProductosAlbaran.append(almacen[oc[3]])  # se añade el producto a la lista
            albaran = oc[1]  # se asigna nuevo id del albaran
            proveedor = oc[2]  # se asigna nuevo proveedor
            linea += 1

        log("Se ha creado una lista nueva de compras")

        return ordenesCompra


"""
////////////////////////////////////////////////////////////////////////////////////
                    CREA OBJETOS DE TIPO ORDEN VENTA CON LA LISTA RECIBIDA
////////////////////////////////////////////////////////////////////////////////////
"""


def montaOrdenesVenta():
    listaProductosAlbaran = []
    listaOrdenesVenta = BBDD.listadoOrdenesVenta()
    montaProductos()
    montaClientes()
    ordenesVenta.clear()
    if listaOrdenesVenta:

        albaran = 0
        cliente = 0
        linea = 0

        for oc in listaOrdenesVenta:  # Recorre todas las filas de la tabla odenes compra

            # si no coincide el albaran con el anterior y no es la primera linea  o si es el ultimo crea orden de venta
            if albaran != oc[1] and linea > 0 or linea == len(listaOrdenesVenta) - 1:
                if linea == len(listaOrdenesVenta) - 1:
                    listaProductosAlbaran.append(almacen[oc[3]])  # se añade el producto a la lista
                    cliente = oc[2]
                    albaran = oc[1]
                # si ha cambiado de venta  se crea la compra
                lista = listaProductosAlbaran.copy()  # se hace una copia porque si no al borrar borra la referencia
                ordenVenta = Clase.OrdenVenta(clientes[cliente], lista, albaran)
                ordenVenta.setId(oc[0])
                ordenesVenta[oc[0]] = ordenVenta  # se guarda en la lista de ordenes de venta con su id
                listaProductosAlbaran.clear()  # se vacia la lista de productos para la siguiente compra

            listaProductosAlbaran.append(almacen[oc[3]])  # se añade el producto a la lista
            albaran = oc[1]  # se asigna nuevo id del albaran
            cliente = oc[2]  # se asigna nuevo proveedor
            linea += 1

        log("Se ha creado una lista nueva de ventas")

        return ordenesVenta
