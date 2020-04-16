import sqlite3
miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()

#crear tabla en la base de datos GestionProductos

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    CODIGO_ARTICULOS VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SELECCION VARCHAR(20)
    )
'''
)

#AGRAGAR DATOS A LA TABLA

productos = [
    ("AR01","pelota",20,"jugueteria"),
    ("AR02","pantalon",15,"confeccion"),
    ("AR03","destornillador",25,"ferreteria"),
    ("AR04","jarron",45,"ceramica")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)",productos)


miConexion.commit()
miConexion.close()