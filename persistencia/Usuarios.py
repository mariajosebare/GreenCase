from persistencia import MySqlConnector


def crearUsuario(email, nombre, apellido, password):
    usuarios = MySqlConnector.correr_sql(f"INSERT INTO usuarios VALUES ('{email}','{nombre}','{apellido}','{password}')")
    return obtenerUsuario(email, password)


def obtenerUsuario(email, password):
    usuarios = MySqlConnector.correr_sql(f"SELECT IdUsuario, Nombre, Apellido FROM usuarios WHERE IdUsuario = '{email}' AND password = '{password}'")
    if usuarios.__len__() == 1:
        return usuarios[0]
    else:
        return None