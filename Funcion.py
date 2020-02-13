import Clase
import Menu

#////////////////////////////////////////////////////////////////////////////////////
#                       MUESTRA LA LISTA DE PROVEEDORES
#////////////////////////////////////////////////////////////////////////////////////
def muestraProveedor():
    repite = True
    while repite:
        i = 1
        for p in Menu.proveedores:
            print(i, ": ", p.getNombre())
            i += 1

        try:
            return int(input("Elige un proveedor: ")) - 1
        except:
            repite = True

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
        Menu.proveedores.append(proveedor)
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
        Menu.productos.append(producto)
        print("{0} Creado!\n".format(producto.getNombre()))

    else:
        print(errores)

