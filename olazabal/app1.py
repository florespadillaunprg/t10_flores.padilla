#EJERCICIO 01
import libreria

#MENU PARA AGREGAR NOMBRES Y DIRECCION
def agregar_nombre():
    input("Ingrese nombre:")
    print("se agrego nombre")
def agregar_direccion():
    input("ingrese direccion:")
    print("se agrego direccion")

#MENU GENERAL
opc=0
max=3
while   (opc!=max):
    print("########################")
    print("######### MENU #########")
    print("#01. Agregar nombre:   #")
    print("#02. Agregar direccion #")
    print("#03. Salir.")
    print("########################")
    opc=libreria.pedir_numero("ingrese numero", 1, 3)
#Fin_menu

#Mapeo de Funciones
    if(opc==1):
        agregar_nombre()
    if(opc==2):
        agregar_direccion()
print("Programa finalizado")
