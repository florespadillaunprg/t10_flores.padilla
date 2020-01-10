import libreria

# Aplicacion para pedir mes , dia y numero de dia

def subOpcionA():
    # 1. Pedir nombre del mes
    # 2. Pedir dia_semana
    # 3. Pedir dia
    # 4. Guardar datos en archivo 3_app.txt
    mes=libreria.pedir_mes("Ingrese mes : ")
    dia_semana=libreria.pedir_dia_semana("Ingrese el dia de la semana : ")
    dia=libreria.pedir_dia("Ingrse dia : ")
    contenido=mes+"-"+dia_semana+"-"+str(dia)+"\n"
    libreria.guardar_datos("3_app.txt", contenido,"a")
    print("Datos agregados")

def subOpcionB():
    print("NOMBRE   DIA-SEMANA   DIA")
    fecha=libreria.obtener_datos_lista("3_app.txt")
    for linea in fecha:
        linea=linea.replace("\n","")
        mes,dia_semana,dia=linea.split("-")
        print(mes+ " - "+ dia_semana + " - "+ dia)
    print("Datos leidos")

def submenu1():
    opc=0
    max=2

    while ( opc != max ):
        print("################################################")
        print("##################  SUBMENU ####################")
        print("################################################")
        print("# 1. Agregar fecha  (subOpcion A)              #")
        print("# 2. Salir                                     #")
        print("################################################")

        opc=libreria.pedir_numero("Ingrese opcion : ",1,2)

        if ( opc == 1 ):
            subOpcionA()
    # fin_submenu1

def submenu2():
    opc=0
    max=2

    while ( opc != max ):
        print("################################################")
        print("##################  SUBMENU ####################")
        print("################################################")
        print("# 1. Leer fecha  (subOpcion B)                 #")
        print("# 2. Salir                                     #")
        print("################################################")

        opc=libreria.pedir_numero("Ingrese opcion : ",1,2)

        if ( opc == 1 ):
            subOpcionB()
    # fin_sub_menu2

#### MENU  ##########

opc=0
max=3

while ( opc != max ):
    print("################################################")
    print("##################  MENU #######################")
    print("################################################")
    print("# 1. Submenu1                                  #")
    print("# 2. Submenu2                                  #")
    print("# 3. Salir                                     #")
    print("################################################")

    opc=libreria.pedir_numero("Ingrese opcion : ",1,3)

    if ( opc == 1 ):
        submenu1()

    if (opc == 2 ):
        submenu2()

#  fin_menu
print("FIN DEL PROGRAMA")

