class Proveedor:

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