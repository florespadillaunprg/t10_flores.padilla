#Ejercicio 04

import libreria

#MENU PARA ELEGIR LA UNIVERSIDAD O COLEGIO
def agregar_universidad():
    libreria.pedir_universidad("Ingrese la universidad:")
    print("Se agrego universidad")
def agregar_colegio():
    libreria.pedir_colegio("Ingrese el colegio:")
    print("Se agrego el colegio")


#MENU GENERAL
opc=0
max=3
while(opc!=max):
    print("#########################")
    print("##########MENU###########")
    print("#1. agregar univesidad")
    print("#2. agregar colegio")
    print("#3. Salir")
    opc=libreria.pedir_numero("ELEGIR OPCION:", 1, 3)

#Fin_menu

#Mapeo_de_funciones
    if ( opc == 1):
        agregar_universidad()
    if(opc==2):
        agregar_colegio()

print("Fin del Programa")

