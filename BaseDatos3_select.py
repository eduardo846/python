import sqlite3

miConexion=sqlite3.connect("PrimeraBase")
miCursor=miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

print(variosProductos)

#O mostrar de otra manera
for producto in variosProductos:
    print(producto[0])

miConexion.commit()

miConexion.close()