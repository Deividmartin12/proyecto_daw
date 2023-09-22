from flask import Flask, render_template, request, redirect, flash, jsonify
import controlador_discos
import controlador_cliente
import controlador_categoria_producto

app = Flask(__name__)

@app.route("/agregar_disco")
def formulario_agregar_disco():
    return render_template("agregar_disco.html")

@app.route("/agregar_cliente")
def formulario_agregar_cliente():
    return render_template("agregar_cliente.html")

@app.route("/agregar_categoria_producto")
def formulario_agregar_categoria_producto():
    return render_template("agregar_categoria.html")

@app.route("/guardar_disco", methods=["POST"])
def guardar_disco():
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    artista = request.form["artista"]
    precio = request.form["precio"]
    genero = request.form["genero"]
    controlador_discos.insertar_disco(codigo, nombre, artista, precio, genero)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/discos")

@app.route("/guardar_cliente", methods=["POST"])
def guardar_cliente():
    nombre = request.form["nombre"]
    apellidos = request.form["apellidos"]
    email = request.form["email"]
    telefono = request.form["telefono"]
    direccion = request.form["direccion"]

    controlador_cliente.insertar_clientes( nombre, apellidos, email, telefono, direccion)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/clientes")


@app.route("/")
@app.route("/discos")
def discos():
    discos = controlador_discos.obtener_discos()
    return render_template("discos.html", discos=discos)


@app.route("/clientes")
def clientes():
    clientes = controlador_cliente.obtener_clientes()
    return render_template("clientes.html", datos_clientes=clientes)

@app.route("/categoria_producto")
def categoria_producto():
    categoria_productos=controlador_categoria_producto.obtener_categoria_producto()
    #datos_cate_prod es la variable donde se guarda la lista de la bd categoria_producto
    return render_template("categoria_producto.html", datos_cate_prod=categoria_productos)

@app.route("/eliminar_disco", methods=["POST"])
def eliminar_disco():
    controlador_discos.eliminar_disco(request.form["id"])
    return redirect("/discos")

@app.route("/eliminar_cliente", methods=["POST"])
def eliminar_cliente():
    controlador_cliente.eliminar_cliente(request.form["cliente_id"])
    return redirect("/clientes")


@app.route("/formulario_editar_disco/<int:id>")
def editar_disco(id):
    # Obtener el disco por ID
    disco = controlador_discos.obtener_disco_por_id(id)
    return render_template("editar_disco.html", disco=disco)

@app.route("/formulario_editar_cliente/<int:cliente_id>")
def editar_cliente(cliente_id):
    # Obtener el cliente por ID
    cliente = controlador_cliente.obtener_cliente_por_id(cliente_id)
    return render_template("editar_cliente.html", ed_cliente=cliente)


@app.route("/actualizar_disco", methods=["POST"])
def actualizar_disco():
    id = request.form["id"]
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    artista = request.form["artista"]
    precio = request.form["precio"]
    genero = request.form["genero"]
    controlador_discos.actualizar_disco(codigo, nombre, artista, precio, genero, id)
    return redirect("/discos")


@app.route("/actualizar_cliente", methods=["POST"])
def actualizar_cliente():
    cliente_id = request.form["cliente_id"]
    nombre = request.form["nombre"]
    apellidos = request.form["apellidos"]
    email = request.form["email"]
    telefono = request.form["telefono"]
    direccion= request.form["direccion"]
    controlador_cliente.actualizar_cliente(cliente_id, nombre, apellidos, email, telefono, direccion)
    return redirect("/clientes")

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
