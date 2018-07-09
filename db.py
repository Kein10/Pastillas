import sqlite3
import  pastilla

DATABASE_NAME = "data.db"
CONN =  sqlite3.connect(DATABASE_NAME)
CREATE_TABLE = '''
        CREATE TABLE IF NOT EXISTS pastillas ( 
        name TEXT,
        cantidad INT,
        hora TEXT);
        '''
INSERT_ROW = "INSERT INTO pastillas (name, cantidad, hora) VALUES (?, ?, "
INSERT_ROW_NOW = INSERT_ROW + "datetime('now')) "
INSERT_ROW_WHEN = INSERT_ROW + "?) "

def init():
    make(CREATE_TABLE)


def make(sql):
    print("Se ejecutara: %s" % sql)
    CONN.cursor().execute(sql)
    CONN.commit()

def INSERT(p):
    if p.momento == "":
        CONN.cursor().execute(INSERT_ROW_NOW, (p.nombre, p.cantidad))
    else:
        CONN.cursor().execute(INSERT_ROW_WHEN, (p.nombre, p.cantidad, p.momento+":00"))
    CONN.commit()

