# -*- coding: utf-8 -*-
from codecs import encode
import mysql.connector
import getpass
import  time
from datetime import datetime
import time as t
from tkinter import messagebox
global resultado
global messagebox

dbConnect={
    'host':'lldk499.servidoresdns.net',
    'user':'qadr580',
    'password':'*******',
    'database':'qadr580',
    

}
def crear_tabla():#crea ok
    conexion=mysql.connector.connect(**dbConnect)
    cursor=conexion.cursor()
    cursor.execute("CREATE TABLE datos1 (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), password VARCHAR(10), apellidos VARCHAR(20), direccion VARCHAR(255), comentario VARCHAR(150))")


#Consultar tabla de la bbdd consulta la base de datos actual
def consultar_bbdd(n):
    global resultado
    global bd
    conexion=mysql.connector.connect(**dbConnect)
    cursor=conexion.cursor()
    sql="Select * from datos1 Where id={}".format(n)
    cursor.execute(sql)
    resultado=cursor.fetchall()
    #print(resultado)
    #print( datos[0],datos[1],datos[2],datos[3],datos[4])
    for datos in resultado:
        #bd=str(datos[1])+" "+datos[2]+" "+datos[3]+" "+str(datos[4])+"\n"
        bd='Nombre--> {}\nContraseña--> {}\nApellidos--> {}\nEmail--> {}'.format(datos[1],datos[2],datos[3],datos[4])
        messagebox.showinfo(message=bd)
        #print(bd)

def registrar(nombre, password,apellidos,direccion,comentario):#registra ok
    #introducir nuevo usuario
    conexion=mysql.connector.connect(**dbConnect)
    cursor=conexion.cursor()
    sql = "INSERT INTO datos1 (nombre,password,apellidos, direccion,comentario) VALUES (%s,%s,%s,%s,%s)"
    val = (nombre, password,apellidos,direccion,comentario)
    cursor.execute(sql, val)
    print(cursor.rowcount, "registro insertado")
    conexion.commit()
    cursor.close()
    conexion.close()

def borrar(n):
    conexion=mysql.connector.connect(**dbConnect)
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM datos1  WHERE  id={}".format(n))
    

    conexion.commit()
def inicio_de_sesion():
    global usuario_usu
    global resultado
    usuario_usu=input("Escriba su Usuario: ")
    prueba=consulta_user(usuario_usu)
    while prueba!=resultado[1]:
        messagebox.showinfo(message="Usuario no registrado, compruebe su usuario:", title="Inicio Usuario")
        inicio_de_sesion()
        #prueba=consulta_user(usuario_usu)
    t.sleep(1)
    #messagebox.showinfo(message="Usuario correcto", title="Inicio Usuario")
    nombre=getpass.getpass("Escriba su contraseña: ")
    while nombre!=resultado[2]:

        messagebox.showinfo(message="Lo siento vuelve a intentarlo", title="Inicio Usuario")
        inicio_de_sesion()
    #messagebox.showinfo(message="contraseña correcta", title="Inicio Usuario")
    print("Bienvenido {} eres nuestro usuario nº {} y tienes el nivel:{}".format(resultado[1],resultado[0],resultado[3]))
def imp():
    print('CONEXION OK')

def actualizar2(nombre,password,apellidos,direccion,comentario,id):
    conexion=mysql.connector.connect(**dbConnect)
    cursor=conexion.cursor()
    sql='''UPDATE datos1 SET nombre=%s,password=%s,apellidos=%s,direccion=%s,comentario=%s WHERE id=%s'''
    val =(nombre,password,apellidos,direccion,comentario,id)
    cursor.execute(sql,val)
    cursor.fetchall()
    print(cursor.rowcount, "registro actualizado")
    conexion.commit()
    cursor.close()
    conexion.close()



#consultar_bbdd(3)
#crear_tabla()
#registrar()
#actualizar2('silvicchu','007777777','Valverde Cuesta','sil@host.com',' ',3)
#borrar(1)

