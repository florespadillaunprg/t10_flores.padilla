import libreria
# EJERCICIO 06
# Conjunto de cursos
def agregar_primer_curso():
    input("ingrese primer curso:")
    print("se agrego nombre")
def agregar_segundo_curso():
    input("ingrese segundo curso:")
    print("se agrego segundo curso:")
def agregar_tercer_curso():
    input("ingrese tercer curso:")
    print("se agrego tercer curso:")


opc=0
max=4

while (opc!=max):
    print("###########MENU#############")
    print("#1. Agregar primer curso:  #")
    print("#2. Agregar segundo curso: #")
    print("#3. Agregar tercer curso:  #")
    print("#4. Salir:                 #")
    print("############################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1,4)
#fin_menu

# Mapeo de funciones
    if(opc==1):
        agregar_primer_curso()
    if(opc==2):
        agregar_segundo_curso()
    if(opc==3):
        agregar_tercer_curso()

print("Programa Finalizado")
