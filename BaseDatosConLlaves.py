import sqlite3
miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()

#crear tabla en la base de datos GestionProductos

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SELECCION VARCHAR(20)
    )
'''
)

#AGRAGAR DATOS A LA TABLA

productos = [
    ("pelota",20,"jugueteria"),
    ("pantalon",15,"confeccion"),
    ("destornillador",25,"ferreteria"),
    ("jarron",45,"ceramica")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)


miConexion.commit()
miConexion.close()