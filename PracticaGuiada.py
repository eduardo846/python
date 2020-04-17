from tkinter import *  #importa libreria para entorno grafico 
from tkinter import messagebox #importar libreria para mensajes emergente
import sqlite3   #importar libreria para trabajar con bases de datos

#=========funciones=================================

def conexionBBDD():
    miConexion=sqlite3.connect("Usuarios")

    miCursor=miConexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIO VARCHAR(100))
            ''')
        messagebox.showinfo("BBDD","BBDD creada con exito")
    except:
        messagebox.showwarning("Atencion","La BBDD ya existe")
    

def salirAplicacion():
    valor=messagebox.askquestion("Salir","Deseas salir de la aplicacion?")
    if valor=="yes":
        root.destroy()


def limpiarCampos():
    miID.set("")
    miNombre.set("")
    miApellido.set("")
    miPass.set("")   
    miDireccion.set("")
    textoComentario.delete(1.0,END)

def crear():
    miConexion=sqlite3.connect("Usuarios")

    miCursor=miConexion.cursor()
    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0", END)
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
    """
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'" + miNombre.get()+
    "','" + miPass.get() +
    "','" + miApellido.get() +
    "','" + miDireccion.get() +
    "','" + textoComentario.get("1.0", END) + "')")
    """
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro insertado con exito")


def leer():
    miConexion=sqlite3.connect("Usuarios")

    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miID.get())

    elUsuario=miCursor.fetchall()
    for usuario in elUsuario:

        miID.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert(1.0,usuario[5])
    miConexion.commit()


def actualizar():
    
    miConexion=sqlite3.connect("Usuarios")

    miCursor=miConexion.cursor()

    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
        "', PASSWORD='" + miPass.get() +
        "', APELLIDO='" + miApellido.get() +
        "', DIRECCION='" + miDireccion.get() +
        "', COMENTARIO='" + textoComentario.get("1.0", END) +
        "' WHERE ID=" + miID.get())

    miConexion.commit()
    messagebox.showinfo("BBDD","Registro actualizado con exito")


def eliminar():
    
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miID.get())

    miConexion.commit()
    messagebox.showinfo("BBDD","Registro borrado con exito")
    

root=Tk()


#Menu superior
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

#Elentos en la barra de menu superior
bbddMenu=Menu(barraMenu,tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=salirAplicacion)

borrarMenu=Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Borrar campos",command=limpiarCampos)

crudMenu=Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Borrar",command=eliminar)

ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD",menu=bbddMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)


#---------------------comienzo de campos ----------------------------------

miFrame=Frame(root)
miFrame.pack()

miID=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()



cuadroID=Entry(miFrame,textvariable=miID)
cuadroID.grid(row=0, column=1,padx=10,pady=10)

cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1, column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="right")

cuadroPass=Entry(miFrame,textvariable=miPass)
cuadroPass.grid(row=2, column=1,padx=10,pady=10)
cuadroPass.config(show="?")

cuadroApellido=Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=3, column=1,padx=10,pady=10)

cuadroDireccion=Entry(miFrame,textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1,padx=10,pady=10)

textoComentario=Text(miFrame,width=16, height=5)
textoComentario.grid(row=5, column=1,padx=10,pady=10)
scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=5,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

#-----------aqui comienzan las etiquetas
idLabel=Label(miFrame,text="Id:")
idLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

passLabel=Label(miFrame,text="Password:")
passLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

direccionLabel=Label(miFrame,text="Direccion:")
direccionLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

comentarioLabel=Label(miFrame,text="Comentario:")
comentarioLabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)


#------aqui los botones inferiores

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2,text="Create",command=crear)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(miFrame2,text="Read",command=leer)
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

botonActualizar=Button(miFrame2,text="Update",command=actualizar)
botonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

botonBorrar=Button(miFrame2,text="Delete",command=eliminar)
botonBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)



root.mainloop()
