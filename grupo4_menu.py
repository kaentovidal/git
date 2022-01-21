import os

from grupo4polimorfismo import *

#librerías necesarias limpiar la pantalla
import os
import time

#función para limpiar pantalla
def limpiar_pantalla():
    time.sleep(3)
    os.system("cls")

#crear objetos de clase paquete (clase hija)
oPerson1=vip("JOSE","1450106545","0963299948",4)

condicion=False
while condicion==False:
    limpiar_pantalla()
    print("========MENU============")
    print("1. Tipo de cliente")
    print("2. Imprimir los datos de socio")
    print("0. Salir")
    
    opcion=int(input("Introduzca la opción deseada: "))
    if opcion==1:
        print ("El cliente es:"),tipe(oPerson1)
    elif opcion==2:
        print("Datos del Socio")
        print("Nombre:", oPerson1.getNombre())
        print("Cedula:", oPerson1.getIdt())
        print("Celular:", oPerson1.getCell())
        print("El descuento es de "),tipo(oPerson1)
    elif opcion==0:
        print ("Adios ...")
        condicion=True
        exit()
