import libreria

#MENU PARA ELEGIR MARCAS DE LAPTOPS
def agregar_marca():
    libreria.pedir_marca("Ingrese la marca:")
    print("Se agrego marca")
def agregar_memoria():
    libreria.pedir_memoria("ingrese cantidad de memoria:")
    print("se agrego cantidad de memoria ")

#MENU GENERAL
opc=0
max=3
while(opc!=3):
    print("#######################")
    print("######## MENU #########")
    print("#1. Ingrese marca de laptop:")
    print("#2. Ingrese cantidad de memoria:")
    print("#3, salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregar_marca()
    if(opc==2):
        agregar_memoria()

print(" fin del programa")
