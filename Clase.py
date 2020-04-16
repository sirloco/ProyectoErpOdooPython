import abc


class Persona(metaclass=abc.ABCMeta):

    # Constructor
    def __init__(self, nombre, direccion):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__id = ""

    def nombre(self):
        return self.__nombre

    def direccion(self):
        return self.__direccion


class Empleado(Persona):

    def __init__(self, nombre, direccion):
        super().__init__(nombre, direccion)
        self.__tipo = '1'

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setTipo(self, tipo):
        self.__tipo = tipo

    def getTipo(self):
        return self.__tipo

    def getNombre(self):
        return super().nombre()

    def getDireccion(self):
        return super().direccion()


class Cliente(Persona):

    def __init__(self, nombre, direccion):
        super().__init__(nombre, direccion)
        self.__tipo = '2'

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setTipo(self, tipo):
        self.__tipo = tipo

    def getTipo(self):
        return self.__tipo

    def getNombre(self):
        return super().nombre()

    def getDireccion(self):
        return super().direccion()


class Proveedor(Persona):

    def __init__(self, nombre, direccion):
        super().__init__(nombre, direccion)
        self.__tipo = '3'

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setTipo(self, tipo):
        self.__tipo = tipo

    def getTipo(self):
        return self.__tipo

    def getNombre(self):
        return super().nombre()

    def getDireccion(self):
        return super().direccion()


class Producto:

    # Constructor
    def __init__(self, nombre, precio, cantidad):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad
        self.__id = ""
        self.__visible = 1

    # Getters y Setters
    def getNombre(self):
        return self.__nombre

    def getPrecio(self):
        return self.__precio

    def setCantidad(self, cantidad):
        self.__cantidad = cantidad

    def getCantidad(self):
        return self.__cantidad

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setVisibilidad(self, visibilidad):
        self.__visible = visibilidad

    def getVisibilidad(self):
        return self.__visible


class OrdenCompra:

    # Constructor
    def __init__(self, proveedor, productos, albaran):
        self.__productos = productos
        self.__proveedor = proveedor
        self.__albaran = albaran
        self.__id = ""

    # Getters y Setters
    def getProductos(self):
        return self.__productos

    def getProveedor(self):
        return self.__proveedor

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def getAlbaran(self):
        return self.__albaran


class OrdenVenta:

    # Constructor
    def __init__(self, cliente, productos, albaran):
        self.__productos = productos
        self.__cliente = cliente
        self.__albaran = albaran
        self.__id = ""

    # Getters y Setters
    def getProductos(self):
        return self.__productos

    def getCliente(self):
        return self.__cliente

    def getAlbaran(self):
        return self.__albaran

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id
