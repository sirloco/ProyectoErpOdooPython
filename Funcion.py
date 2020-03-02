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
                return int(input("Elige un producto o inserta 0 para crear uno nuevo: ")) - 1
            except:
                repite = True
        else:
            repite = False
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
                return int(input("Elige un cliente o pon un n para crear uno nuevo: ")) - 1
            except:
                repite = True
        else:
            repite = False
#////////////////////////////////////////////////////////////////////////////////////
#                       MUESTRA LA LISTA DE ORDENES DE COMPRA
#////////////////////////////////////////////////////////////////////////////////////
def muestraOrdenesCompra(quiereUnaConcreta):
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
#////////////////////////////////////////////////////////////////////////////////////
#                                  CREA ORDEN DE COMPRA
#////////////////////////////////////////////////////////////////////////////////////
def nuevaOrden():
    errores = False

    if not errores:
        #Me interesa crear una lista de productos cada vez que se llame a esta funcion
        listaProductos = {}

        proveedorElegido = muestraProveedor()

        if proveedorElegido is None or proveedorElegido < 0:
            print("-Creando nuevo Proveedor-")
            creaProveeodor()
            proveedorElegido = len(almacen) - 1

        repite = True
        while repite:
            productoElegido = muestraProductos(True)

            if productoElegido is None or productoElegido < 0:
                print("-Creando Nuevo Producto-")
                nuevoProducto()
                productoElegido = len(almacen) -1

            cantidad = input("cantidad: ").strip()

            listaProductos[almacen[productoElegido]] = cantidad

            respuesta = input("¿Agregar otro producto? (s/n)").strip()

            repite = False if respuesta == "n" else True

        ordenCompra = Clase.OrdenCompra(proveedores[proveedorElegido], listaProductos)
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
#                           ELIMINAR CLIENTE
#////////////////////////////////////////////////////////////////////////////////////
def eliminaCliente():
    eligeUno = True
    clienteElegido = muestraProductos(eligeUno)
    print("Nada que borrar\n" if clienteElegido is None else clientes.pop(clienteElegido).getNombre() + " Eliminado\n")
