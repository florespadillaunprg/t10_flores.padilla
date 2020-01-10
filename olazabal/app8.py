#Ejercicio 08
import libreria

#MENU PARA ELEGIR LOS CONTINENTES
def agregar_continentes():
    libreria.pedir_continente("ingrese continente:")
    print("se guardo continente")

opc=0
max=2

#MENU GENERAL
#EN ESTE MENU TENDREMOS 2 OPCIONES (1-2)
#EN LA OPCION 1 PODREMOS INGRESAR EL NOMBRE DEL CONTINENTE
while ( opc != max):
    print("############################")
    print("######### MENU #############")
    print("############################")
    print("#1. agregar continentes:")
    print("#############################")
    opc=libreria.pedir_numero("ingrese opcion;",1 ,2)


#Fin_menu

#Mapeo de Funciones
    if(opc==1):
        agregar_continentes()

print("Programa finalizado")

