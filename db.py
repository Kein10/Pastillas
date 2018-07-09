import sqlite3
import  pastilla

DATABASE_NAME = "data.xd"
CONN =  sqlite3.connect(DATABASE_NAME)
CREATE_TABLE = '''
        CREATE TABLE IF NOT EXISTS pastillas (
        id INTEGER AUTOINCREMENTE PRIMARY KEY, 
        name TEXT,
        cantidad INT,
        hora TEXT);
        '''
INSERT_ROW = '''
                INSERT INTO pastillas
                (name, cantidad, hora)
                VALUES (?, ?, NOW())
            '''


def init():
    make(CREATE_TABLE)


def make(sql):
    print("Se ejecutará: %s" % sql)
    CONN.cursor().execute(sql)
    CONN.commit()

def INSERT(nombre, cantidad, momento):
    CONN.cursor().execute("INSERT INTO pastillas (name, cantidad, hora) VALUES (?, ?, NOW()) ", (nombre, cantidad, momento))
    CONN.commit()


init()
p = pastilla.Pastilla("Sukrol", 3, "")
INSERT_ROW(p)

