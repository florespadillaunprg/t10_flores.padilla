#Ejercicio 02
import libreria

#MENU PARA PEDIR SEXO: FEMENINO O MASCULINO
def agregar_sexo():
    libreria.pedir_sexo("Ingrese el sexo:")
    print("Se agrego sexo")


#MENU GENERAL
opc=0
max=3
while(max== 3):
    print("#########################")
    print("##########MENU###########")
    print("#1. Sexo:masculino")
    print("#2. Sexo:femenino")
    print("#3. Salir")
    opc=libreria.pedir_numero("Elegir numero:", 1, 3)

#Fin_menu

#Mapeo_de_funciones
    if ( opc == 1):
        agregar_sexo()
    if ( opc == 2):
        agregar_sexo()


print("Fin del Programa")
