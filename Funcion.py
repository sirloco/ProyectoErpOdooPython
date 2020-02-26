import Clase

# lista de proveedores
proveedores = []
almacen = []
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
def muestraProductos():
    repite = True
    while repite:
        i = 1
        for p in almacen:
            print(i, ": ", p.getNombre())
            i += 1

        try:
            return int(input("Elige un producto o pon un 0 para crear uno nuevo: ")) - 1
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

    if len(proveedores) < 1: errores = "Deben existir al menos un proveedor"
    print(len(proveedores))
    if not errores:
        proveedorElegido = muestraProveedor()

        productoElegido = muestraProductos()

        if productoElegido == -1:
            nuevoProducto()
            productoElegido = len(almacen) -1

        cantidad = input("cantidad: ").strip()

        ordenCompra = Clase.OrdenCompra(proveedores[proveedorElegido],almacen[productoElegido],cantidad)
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

        proveedor = Clase.Proveedor(nombre, direccion)
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

