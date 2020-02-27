import Clase

# lista de proveedores
proveedores = []
almacen = []
clientes = []
ordenesCompra = []

#////////////////////////////////////////////////////////////////////////////////////
#                       MUESTRA LA LISTA DE PROVEEDORES
#////////////////////////////////////////////////////////////////////////////////////
def muestraProveedor():
    repite = True
    while repite:
        i = 1
        for pro in proveedores:
            print(i, ": ", pro.getNombre())
            i += 1

        try:
            return int(input("Elige un proveedor: ")) - 1
        except:
            repite = True
#////////////////////////////////////////////////////////////////////////////////////
#                       MUESTRA LA LISTA DE PRODUCTOS
#////////////////////////////////////////////////////////////////////////////////////
def muestraProductos(quiereUnoConcreto):
    repite = True if len(almacen) > 0 else False

    while repite:
        i = 1
        for p in almacen:
            print(i, ": ", p.getNombre())
            i += 1

        if quiereUnoConcreto:
            try:
                return int(input("Elige un producto o pon un 0 si no está el que buscas: ")) - 1
            except:
                repite = True
#////////////////////////////////////////////////////////////////////////////////////
#                       MUESTRA LA LISTA DE CLIENTES
#////////////////////////////////////////////////////////////////////////////////////
def muestraClientes(quiereUnoConcreto):
    repite = True if len(clientes) > 0 else False

    while repite:
        i = 1
        for c in clientes:
            print(i, ": ", c.getNombre())
            i += 1

        if quiereUnoConcreto:
            try:
                return int(input("Elige un cliente o pon un 0 si no está el que buscas: ")) - 1
            except:
                repite = True
#////////////////////////////////////////////////////////////////////////////////////
#                       MUESTRA LA LISTA DE ORDENES DE COMPRA
#////////////////////////////////////////////////////////////////////////////////////
def muestraOrdenesCompra():#todo esto esta por terminar
    repite = True
    while repite:
        i = 1
        for oc in ordenesCompra:
            #print(i, ": ", oc.getProveedor())
            i += 1

        try:
            return int(input("Elige un proveedor: ")) - 1
        except:
            repite = True
#////////////////////////////////////////////////////////////////////////////////////
#                                  CREA ORDEN DE COMPRA
#////////////////////////////////////////////////////////////////////////////////////
def nuevaOrden():
    errores = False

    if len(proveedores) < 1: errores = "Deben existir al menos un proveedor\n"
    if not errores:
        proveedorElegido = muestraProveedor()

        productoElegido = muestraProductos(True)

        if productoElegido == -1:
            nuevoProducto()
            productoElegido = len(almacen) -1

        cantidad = input("cantidad: ").strip()

        ordenCompra = Clase.OrdenCompra(proveedores[proveedorElegido], almacen[productoElegido], cantidad)
        ordenesCompra.append(ordenCompra)
        print("Orden Creada!\n")


        print("nueva orden de compra")
    else:
        print(errores)
#////////////////////////////////////////////////////////////////////////////////////
#                            CREA PROVEEDOR NUEVO
#////////////////////////////////////////////////////////////////////////////////////
def creaProveeodor():
    errores = False
    nombre = input("Nombre: ").strip()
    direccion = input("Direccion: ").strip()

    if nombre == "" or direccion == "": errores = "Error, campos obligatorios!"

    if not errores:

        proveedor = Clase.Persona(nombre, direccion)
        proveedores.append(proveedor)
        print("{0} Creado!\n".format(proveedor.getNombre()))

    else:
        print(errores)
#////////////////////////////////////////////////////////////////////////////////////
#                           CREA PRODUCTO NUEVO
#////////////////////////////////////////////////////////////////////////////////////
def nuevoProducto():
    errores = False
    nombre = input("Nombre: ").strip()
    precio = input("Precio: ").strip()

    if nombre == "" or precio == "": errores = "Error, campos obligatorios!"

    if not errores:

        producto = Clase.Producto(nombre, precio)
        almacen.append(producto)
        print("{0} Creado!\n".format(producto.getNombre()))

    else:
        print(errores)
#////////////////////////////////////////////////////////////////////////////////////
#                           CREA CLIENTE NUEVO
#////////////////////////////////////////////////////////////////////////////////////
def nuevoCliente():
    errores = False
    nombre = input("Nombre: ").strip()
    direccion = input("Direccion: ").strip()

    if nombre == "" or direccion == "": errores = "Error, campos obligatorios!"

    if not errores:
        cliente = Clase.Producto(nombre, direccion)
        clientes.append(cliente)
        print("{0} Creado!\n".format(cliente.getNombre()))

    else:
        print(errores)
#////////////////////////////////////////////////////////////////////////////////////
#                           ELIMINAR PRODUCTO
#////////////////////////////////////////////////////////////////////////////////////
def eliminaProducto():
    eligeUno = True
    productoElegido = muestraProductos(eligeUno)
    print("Nada que borrar\n" if productoElegido is None else almacen.pop(productoElegido).getNombre() + " Eliminado\n")
#////////////////////////////////////////////////////////////////////////////////////
#                           ELIMINAR PRODUCTO
#////////////////////////////////////////////////////////////////////////////////////
def eliminaCliente():
    eligeUno = True
    clienteElegido = muestraProductos(eligeUno)
    print("Nada que borrar\n" if clienteElegido is None else clientes.pop(clienteElegido).getNombre() + " Eliminado\n")
