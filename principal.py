# -*- coding: utf-8 -*-
#!/usr/bin/python
import getpass
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import tkinter as tk
from bbdd import *


class Cuestionario:

    def __init__(self):
        self.id=''
        self.nombre=''
        self.password=''
        self.apellidos=''
        self.direccion=''
        self.comentario=''

    def ingresar_usuario(self):
        self.nombre=vnombre.get()#input('Introduce tu nombre completo: ')
        self.password=vpassword.get()#getpass.getpass("Introduzca su contraseña: ")
        self.apellidos=vapellidos.get()#input('Introduzaca sus apellidos: ')
        self.direccion=vdireccion.get()#input('Introduzca su dirección: ')
        self.comentario=vcomentario.get()#input('Introduzca su comentario: ')
        registrar(c.nombre,c.password,c.apellidos,c.direccion,c.comentario)
        self.nombre=vnombre.set('')
        self.password=vpassword.set('')
        self.apellidos=vapellidos.set('')
        self.direccion=vdireccion.set('')
        self.comentario=vcomentario.set('')

    def borrar_usuario(self):
        self.id=vid.get()
        borrar(c.id)
        self.id=vid.set('')



    def interfaz(self):
      
        self.raiz=Tk()
        self.nombre_usuario="Cuestionario"
        self.raiz.geometry("280x450+0+0")
        self.raiz.iconbitmap("rubik.ico")
        self.raiz.title(self.nombre_usuario)
        #self.fondo=PhotoImage(file="Repite Botella/myAvatari (1).gif",width=203,height=248)
        #self.lblFondo=Label(self.raiz,image=self.fondo).place(x=0,y=0)
        # Crear el menu principal
        global vnombre
        global vapellidos
        global vdireccion
        global vcomentario
        global vid
        global vpassword

        vnombre=StringVar()
        vapellidos=StringVar()
        vid=StringVar()
        vdireccion=StringVar()
        vcomentario=StringVar()
        vpassword=StringVar()

        def hola():
            print( "Hola!")
        menubarra = Menu(self.raiz)

        # Crea un menu desplegable y lo agrega al menu barra
        menuarchivo = Menu(menubarra, tearoff=0)
        menuarchivo.add_command(label="Conectar", command=hola)
        menuarchivo.add_separator()
        menuarchivo.add_command(label="Salir", command=self.raiz.quit)
        menubarra.add_cascade(label="BBDD", menu=menuarchivo)

        # Crea dos menus desplegables mas
        menueditar = Menu(menubarra, tearoff=0)
        menueditar.add_command(label="Borrar campos", command=hola)
        menubarra.add_cascade(label="Borrar", menu=menueditar)
        
        menuayuda = Menu(menubarra, tearoff=0)
        menuayuda.add_command(label="Crear", command=c.ingresar_usuario)
        menuayuda.add_command(label="Leer", command=hola)
        menuayuda.add_command(label="Actualizar", command=hola)
        menuayuda.add_command(label="Borrar", command=c.borrar_usuario)
        menubarra.add_cascade(label="CRUD", menu=menuayuda)

        menuayuda2 = Menu(menubarra, tearoff=0)
        menuayuda2.add_command(label="Licencia", command=hola)
        menuayuda2.add_command(label="Acerca de...", command=hola)
        menubarra.add_cascade(label="Ayuda", menu=menuayuda2)

        self.etiqueta_id=Label(self.raiz,text="Id").place(x=30, y=20) 
        self.espacio0=Entry(self.raiz,justify=RIGHT,textvariable=vid).place(x=130, y=20,)
        
        self.etiqueta_nombre=Label(self.raiz,text="Nombre").place(x=30, y=50)
        self.espacio1=Entry(self.raiz,justify=RIGHT,textvariable=vnombre).place(x=130, y=50)
        
        self.etiqueta_contraseña=Label(self.raiz,text="Contraseña").place(x=30, y=90)
        self.espacio2=Entry(self.raiz,show="*" ,justify=RIGHT,textvariable=vpassword).place(x=130, y=90)
        
        self.etiqueta_apellidos=Label(self.raiz,text="Apellidos").place(x=30, y=130)
        self.espacio3=Entry(self.raiz,justify=RIGHT,textvariable=vapellidos).place(x=130, y=130)
        
        self.etiqueta_direccion=Label(self.raiz,text="Direccion").place(x=30, y=170)
        self.espacio4=Entry(self.raiz,justify=RIGHT,textvariable=vdireccion).place(x=130, y=170)
        
        self.etiqueta_comentario=Label(self.raiz,text="Comentario").place(x=30, y=210)
        texto = Text(self.raiz)
        texto.place(x=130, y=210,textvariable=vcomentario)

        texto.config(width=12, height=5, 
             padx=15, pady=15, selectbackground="red")

        self.boton7=Button(self.raiz,text="Crear", command=c.ingresar_usuario).place(x=20,y=350)
        self.boton8=Button(self.raiz,text="Leer").place(x=80,y=350)
        self.boton9=Button(self.raiz,text="Actualizar").place(x=140,y=350)
        self.boton10=Button(self.raiz,text="Borrar", command=c.borrar_usuario).place(x=220,y=350)
        #self.espaciox.pack()
        Label(self.raiz).pack()



# Mostrar el menu
        self.raiz.config(menu=menubarra)


       
    



        self.raiz.mainloop()

c= Cuestionario()
#c.ingresar_usuario()
c.interfaz()

