import sqlite3

miConexion=sqlite3.connect("PrimeraBase")
miCursor=miConexion.cursor()


variosProductos=[
    
    ("Camisa",10,"Deportes"),
    ("Jarron",90,"Ceramica"),
    ("Camion",20,"Juegueteria")


]
miCursor.executemany("Insert into PRODUCTOS VALUES(?,?,?)",variosProductos)

miConexion.commit()

miConexion.close()