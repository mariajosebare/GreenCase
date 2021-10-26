from flask import Flask, request, jsonify
from persistencia import Usuarios, Modulos


app = Flask(__name__)


#Agregar un usuario
@app.route("/usuarios", methods=['PUT'])
def nuevoUsuario():
    email = request.form['email']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    password = request.form['password']
    usuario = Usuarios.crearUsuario(email, nombre, apellido, password)
    return jsonify(usuario)


#Obtener un usuario según su email y contraseña
@app.route("/login", methods=['POST'])
def obtenerUsuario():
    email = request.form['email']
    password = request.form['password']
    usuario = Usuarios.obtenerUsuario(email, password)
    return jsonify(usuario)


#Agregar un módulo
@app.route("/modulos", methods=['PUT'])
def nuevoModulo():
    idModulo = request.form['id_modulo']
    idUsuario = request.form['id_usuario']
    modulos = Modulos.crearModulo(idModulo, IdUsuario)
    return jsonify()


#Obtiene los datos de un módulo
@app.route("/modulos/<id_modulo>", methods=["GET"])
def obtenerModulo(id_modulo):

    return None



if __name__ == "__main__":
    app.run(debug=True)