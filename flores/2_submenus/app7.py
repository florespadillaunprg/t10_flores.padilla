import libreria

# Aplicacion para pedir ojetos y sus respevtivos costos

def subOpcionA():
    # 1. Pedir nombre
    # 2. Pedir edad
    # 3. Guardar datos en archivo 7_app.txt
    nombre_objeto=libreria.pedir_nombre("Ingrese nombre del objeto : ")
    precio=libreria.pedir_precio("Ingrese precio : ")
    contenido=nombre_objeto+"-"+str(precio)+"\n"
    libreria.guardar_datos("7_app.txt", contenido,"a")
    print("Datos agregados")

def subOpcionB():
    print("NOMBRE DEL OBJETO    Precio")
    objetos=libreria.obtener_datos_lista("7_app.txt")
    for linea in objetos:
        linea=linea.replace("\n","")
        nnombre_ojeto,precio=linea.split("-")
        print(nnombre_ojeto+ "              -  "+ precio)
    print("Datos leidos")

def submenu1():
    opc=0
    max=2

    while ( opc != max ):
        print("################################################")
        print("##################  SUBMENU ####################")
        print("################################################")
        print("# 1. Agregar nombre objeto (subOpcion A)       #")
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
        print("# 1. Leer nombre objeto (subOpcion B)          #")
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

