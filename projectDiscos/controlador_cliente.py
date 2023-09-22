from bd import obtener_conexion


def insertar_clientes( nombre, apellido, email, telefono, direccion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO clientes(nombre, apellidos, email, telefono, direccion) VALUES (%s, %s, %s, %s, %s)",
                       ( nombre, apellido, email, telefono, direccion))
    conexion.commit()
    conexion.close()


def obtener_clientes():
    conexion = obtener_conexion()
    datos_clientes = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT cliente_id, nombre, apellidos, email, telefono, direccion FROM clientes")
        datos_clientes = cursor.fetchall()
    conexion.close()
    return datos_clientes


def eliminar_cliente(cliente_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM clientes WHERE cliente_id = %s", (cliente_id,))
    conexion.commit()
    conexion.close()


def obtener_cliente_por_id(cliente_id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT cliente_id, nombre, apellidos, email, telefono, direccion FROM clientes WHERE cliente_id = %s", (cliente_id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego


def actualizar_cliente(cliente_id, nombre, apellidos, email, telefono, direccion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE clientes SET  nombre = %s, apellidos = %s, email = %s, telefono = %s, direccion=%s WHERE cliente_id = %s",
                       (nombre, apellidos, email, telefono, direccion, cliente_id))
    conexion.commit()
    conexion.close()


