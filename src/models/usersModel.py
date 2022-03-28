from src.config.database import db


def createUser(name,email,password):
    cursor = db.cursor()
    cursor.execute("insert into user (name,email,password) values(%s,%s,%s)", (
        name,
        email,
        password,
    ))
    cursor.close()

