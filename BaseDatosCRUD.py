import sqlite3
miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()

#Mostar
miCursor.execute("SELECT *FROM PRODUCTOS WHERE SELECCION='confeccion'")
productos=miCursor.fetchall()
print(productos)
#actualizar
miCursor.execute("UPDATE  PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

#borrar
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")

miConexion.commit()
miConexion.close()