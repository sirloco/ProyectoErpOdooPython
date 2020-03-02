class Persona:

    # Constructor
    def __init__(self, nombre, direccion):
        self.__nombre = nombre
        self.__direccion = direccion

    # Getters y Setters
    def getNombre(self):
        return self.__nombre
    def getdireccion(self):
        return self.__direccion

class Producto:

    #Constructor
    def __init__(self,nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    #Getters y Setters
    def getNombre(self):
        return self.__nombre
    def getPrecio(self):
        return self.__precio

class OrdenCompra:

    __productos = {}

    #Constructor
    def __init__(self, proveedor, productos):
        self.__productos = productos
        self.__proveedor = proveedor

    #Getters y Setters
    def getProductos(self):
        return self.__productos
    def getProveedor(self):
        return self.__proveedor