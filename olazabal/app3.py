#Ejercicio 03

import libreria

#MENU PARA PEDIR OPERADORES
def agregar_operador():
    libreria.pedir_operador("Ingrese el operador:")
    print("Se agrego operador")

#MENU GENERAL
opc=0
max=5
while(max == 5):
    print("#########################")
    print("##########MENU###########")
    print("#1. sustraendo")
    print("#2. diferencia")
    print("#3. multiplicador")
    print("#4. division")
    print("#5. Salir")
    opc=libreria.pedir_numero("Elegir numero:", 1, 5)

#Fin_menu

#Mapeo_de_funciones
    if ( opc == 1):
        agregar_operador()
    if ( opc == 2):

        agregar_operador()
    if ( opc == 3):
        agregar_operador()
    if ( opc == 4):
        agregar_operador()

print("Fin del Programa")

