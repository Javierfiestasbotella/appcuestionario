# -*- coding: utf-8 -*-
from codecs import encode
import mysql.connector
import getpass
import  time
from datetime import datetime
import time as t
#import saimon.py
from tkinter import messagebox
global resultado
global messagebox

dbConnect={
    'host':'lldk499.servidoresdns.net',
    'user':'qadr580',
<<<<<<< HEAD
    'password':'******',
=======
    'password':'********',
>>>>>>> d90e15d8b94cee591901afd5eb3ae295bd7db219
    'database':'qadr580',
    

}
def crear_tabla():#crea ok
    conexion=mysql.connector.connect(**dbConnect)
    cursor=conexion.cursor()
    cursor.execute("CREATE TABLE datos1 (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), password VARCHAR(10), apellidos VARCHAR(20), direccion VARCHAR(255), comentario VARCHAR(150))")
    #cursor.execute('CREATE TABLE DATOS (ID INTEGER PRIMARY KEY AUTO_INCREMENT,NOMBRE VARCHAR(50),PASSWORD VARCHAR(10), APELLIDOS VARCHAR(20),DIRECCION VARCHAR(20),COMENTARIO(150))')


#Consultar tabla de la bbdd consulta la base de datos actual
def consultar_bbdd():
    global resultado
    global bd
    conexion=mysql.connector.connect(**dbConnect)
    cursor=conexion.cursor()
    sql="Select * from datos1"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    #print(resultado)
    for datos in resultado:
        bd=str(datos[0])+" "+datos[1]+" "+datos[2]+" "+str(datos[3])+"\n"
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

def actualizar(lugar,cambio,antes):
    conexion=mysql.connector.connect(**dbConnect)
    cursor=conexion.cursor()
    #sql = "UPDATE datos1 SET nombre = 'jose' WHERE nombre = 'Frncisco javier'"
    sql = "UPDATE datos1 SET {} = {} WHERE {} = {}".format(lugar,cambio,lugar,antes)

    cursor.execute(sql)

    conexion.commit()

    print(cursor.rowcount, "registros afectado/s")
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
    cursor.execute("UPDATE datos1 SET NOMBRE='" + nombre +
    "',PASSWORD='" + password +
    "',APELLIDOS='" + apellidos +
    "',DIRECCION='" + direccion +
    "',COMENTARIO='" + comentario +
    "'WHERE ID=" + id)
    conexion.commit()

    messagebox.showinfo('BBDD', "Registro actualizado con exito")


#consultar_bbdd()

#crear_tabla()
#registrar()
#actualizar()
#borrar(1)

