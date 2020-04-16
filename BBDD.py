import pymysql

CLIENTE = '2'  # 2 es un valor inventando para identificar a los clientes en la base de datos
PROVEEDOR = '3'
EMPLEADO = '1'


def conectaBD():
    bd = pymysql.connect(host="127.0.0.1", user="root", password="adlocal01", db="odoo", port=3306)
    return bd


"""
////////////////////////////////////////////////////////////////////////////////////
                       EJECUTA SQL EN LA BASE DE DATOS
////////////////////////////////////////////////////////////////////////////////////
"""


def ejecuta(sql):
    # Se obtiene la conecion con la base de datos
    db = pymysql.connect(host="127.0.0.1", user="root", password="adlocal01", db="odoo", port=3306)
    print(sql)
    # Preparar el cursor
    cursor = db.cursor()
    # si la sentencia empieza por s de select devolvemos filas si no hacemos commit
    mostrar = True if sql[0].upper() == 'S' else False
    try:
        # Ejecutar el comando SQL
        cursor.execute(sql)

        resultados = True
        if mostrar:
            resultados = cursor.fetchall()
        else:
            # Aceptar cambios con commit
            db.commit()

        # Desconexión
        db.close()

        return resultados

    except:
        # Rollback en caso de haber algún error
        db.rollback()
        # Desconexión
        db.close()
        return False


"""
////////////////////////////////////////////////////////////////////////////////////
                            MUESTRA PRODUCTO
////////////////////////////////////////////////////////////////////////////////////
"""


def listadoProductos():
    return ejecuta("SELECT * FROM productos")


"""
////////////////////////////////////////////////////////////////////////////////////
                            MUESTRA PERSONA
////////////////////////////////////////////////////////////////////////////////////
"""


def listadoPersonas(tipo):
    return ejecuta("SELECT * FROM personas WHERE tipo LIKE '%" + tipo + "%';")


"""
////////////////////////////////////////////////////////////////////////////////////
                            MUESTRA ORDENES DE COMPRA
////////////////////////////////////////////////////////////////////////////////////
"""


def listadoOrdenesCompra():
    return ejecuta("SELECT * FROM compras")


"""
////////////////////////////////////////////////////////////////////////////////////
                            MUESTRA ORDENES DE VENTA
////////////////////////////////////////////////////////////////////////////////////
"""


def listadoOrdenesVenta():
    return ejecuta("SELECT * FROM ventas")


"""
////////////////////////////////////////////////////////////////////////////////////
                            GUARDA PERSONA
////////////////////////////////////////////////////////////////////////////////////
"""


def guardaPersona(persona):
    return ejecuta('INSERT INTO personas(nombre,direccion,tipo) VALUES ("'
                   + persona.nombre() + '", "' + persona.direccion() + '", ' + persona.getTipo() + ');')


"""
////////////////////////////////////////////////////////////////////////////////////
                              GUARDA PRODUCTO
////////////////////////////////////////////////////////////////////////////////////
"""


def guardaProducto(producto):
    return ejecuta(
        'INSERT INTO productos(nombre,precio,stock) VALUES ("'
        + producto.getNombre() + '", "' + producto.getPrecio() + '", "' + producto.getCantidad() + '");')


"""
////////////////////////////////////////////////////////////////////////////////////
                              GUARDA ORDEN COMPRA
////////////////////////////////////////////////////////////////////////////////////
"""


def guardaOrdenCompra(ordenCompra):
    resultado = True
    for producto in ordenCompra.getProductos():
        resultado = ejecuta('INSERT INTO compras(id_compra,proveedor,articulo,cantidad) VALUES ("'
                            + str(ordenCompra.getAlbaran()) + '", "'
                            + str(ordenCompra.getProveedor().getId()) + '", "'
                            + str(producto.getId()) + '", "'
                            + str(producto.getCantidad()) + '");')

    return resultado


"""
////////////////////////////////////////////////////////////////////////////////////
                              GUARDA ORDEN VENTA
////////////////////////////////////////////////////////////////////////////////////
"""


def guardaOrdenVenta(ordenVenta):
    resultado = True
    for producto in ordenVenta.getProductos():
        resultado = ejecuta('INSERT INTO ventas(id_venta,cliente,articulo,cantidad) VALUES ("'
                            + str(ordenVenta.getAlbaran()) + '", "'
                            + str(ordenVenta.getCliente().getId()) + '", "'
                            + str(producto.getId()) + '", "'
                            + str(producto.getCantidad()) + '");')

    return resultado


"""
////////////////////////////////////////////////////////////////////////////////////
                              ELIMINA PRODUCTO
////////////////////////////////////////////////////////////////////////////////////
"""


def bajaProducto(id):
    return ejecuta('UPDATE productos SET VISIBLE = 0 WHERE id = ' + str(id))


"""
////////////////////////////////////////////////////////////////////////////////////
                              ELIMINA PERSONA
////////////////////////////////////////////////////////////////////////////////////
"""

#todo en vez de eliminar la persona hay que ponerla en invisible como se hace con el producto
def bajaPersona(id):
    return ejecuta('DELETE FROM personas WHERE id = ' + str(id))


"""
////////////////////////////////////////////////////////////////////////////////////
                              ELIMINA ORDEN DE COMPRA
////////////////////////////////////////////////////////////////////////////////////
"""


def bajaOrdenCompra(albaran):
    return ejecuta('DELETE FROM compras WHERE id_compra = ' + str(albaran))


"""
////////////////////////////////////////////////////////////////////////////////////
                              ELIMINA ORDEN DE VENTA
////////////////
////////////////////////////////////////////////////////////////////
"""


def bajaOrdenVenta(albaran):
    return ejecuta('DELETE FROM ventas WHERE id_venta = ' + str(albaran))
