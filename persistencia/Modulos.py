from persistencia import MySqlConnector


def crearModulo(idModulo,IdUsuario):
    modulos = MySqlConnector.insertar_sql(f"INSERT INTO modulos VALUES ('{idModulo}','{IdUsuario}')")
    if modulos.__len__() == 1:
        return modulos[0]
    else:
        return None


def obtenerModulo(id_modulo):
    modulos = MySqlConnector.correr_sql(f"SELECT * FROM modulos WHERE IdModulo='{id_modulo}'")
    if modulos.__len__() ==1:
        return modulos[0]
    else:
        return None
                