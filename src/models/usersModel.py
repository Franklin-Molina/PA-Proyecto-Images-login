from src.config.database import db


def createUser(name,email,claveEncritada):
    cursor = db.cursor()
    cursor.execute("insert into user (name,email,password) values(%s,%s,%s)", (
        name,
        email,
        claveEncritada,
    ))
    cursor.close()

def validarUser(self,usuario):
        cursor = db.cursor()
        cursor.execute('select correo, password from usuario where usuario.correo = %s',(usuario,))
        usuario = cursor.fetchall()
        cursor.close()
        return usuario

