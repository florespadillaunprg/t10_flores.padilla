import libreria

# Aplicacion para pedir dia , mes , anio

def subOpcionA():
    # 1. Pedir dia
    # 2. Pedir mes
    # 3. Pedir anio
    # 4. Guardar datos en archivo 8_app.txt
    dia=libreria.pedir_dia_semana("Ingrese el dia : ")
    mes=libreria.pedir_mes("Ingrese el mes : ")
    anio=libreria.pedir_anio("Ingrese el anio : ")
    contenido=dia+"-"+mes+ "-"+str(anio)+"\n"
    libreria.guardar_datos("8_app.txt", contenido,"a")
    print("Datos agregados")

def subOpcionB():
    print("DIA         MES         ANIO")
    objetos=libreria.obtener_datos_lista("8_app.txt")
    for linea in objetos:
        linea=linea.replace("\n","")
        dia,mes,anio=linea.split("-")
        print(dia+ " - "+ mes+" - "+anio)
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
    print("# 4. Salir                                     #")
    print("################################################")

    opc=libreria.pedir_numero("Ingrese opcion : ",1,3)

    if ( opc == 1 ):
        submenu1()

    if (opc == 2 ):
        submenu2()

#  fin_menu
print("FIN DEL PROGRAMA")

