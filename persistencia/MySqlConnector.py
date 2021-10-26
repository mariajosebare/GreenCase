import pymysql


__cursor = pymysql.connect(
    host = "127.0.0.1",
    user="root",
    password="root",
    db="green_case",
    cursorclass=pymysql.cursors.DictCursor
).cursor()


def correr_sql(query):
    __cursor.execute(query)
    __cursor.connection.commit()
    return __cursor.fetchall()


def insertar_sql(query):
    __cursor.execute(query)
    __cursor.connection.commit()
    return __cursor.lastrowid