from bd import obtener_conexion

def obtener_categoria_producto():
    conexion = obtener_conexion()
    datos_cate_producto=[]
    with conexion.cursor() as cursor:
        cursor.execute('SELECT categoria_id, nombre FROM categoria_producto')
        datos_cate_producto = cursor.fetchall()
    conexion.close()
    return datos_cate_producto