
import libreria
#EJERCICIO 7

def agregar_primera_facultad():
    input("ingrese nombre:")
    print("se agrego nombre:")
def agregar_segunda_facultad():
    input("ingrese nombre:")
    print("se agrego nombre:")

opc=0
max=3
while (opc!=max):
    print("############# MENU ############")
    print("#1. Agregar primera facultad: #")
    print("#2. Agregar segunda facultad: #")
    print("#3. Salir.                    #")
    print("###############################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)
#fin_menu

# Mapeo de funciones
    if(opc==1):
        agregar_primera_facultad()
    if(opc==2):
        agregar_segunda_facultad()
print("Programa Finalizado")

#fin_def

#fin_def
