import libreria

# Aplicacion para pedir nombres y apellidos completos

def subOpcionA():
    # 1. Pedir nombre
    # 2. Pedir edad
    # 3. Guardar datos en archivo 1_app.txt
    nombre=libreria.pedir_nombre("Ingrese nombre : ")
    edad=libreria.pedir_numero("Ingrese edad : ",0,100)
    contenido=nombre+"-"+str(edad)+"\n"
    libreria.guardar_datos("1_app.txt", contenido,"a")
    print("Datos agregados")

def subOpcionB():
    print("NOMBRE   EDAD")
    nombres=libreria.obtener_datos_lista("1_app.txt")
    for linea in nombres:
        linea=linea.replace("\n","")
        nombre,edad=linea.split("-")
        print(nombre+ "  -  "+ edad)
    print("Datos leidos")

def submenu1():
    opc=0
    max=2

    while ( opc != max ):
        print("################################################")
        print("##################  SUBMENU ####################")
        print("################################################")
        print("# 1. Agregar nombre (subOpcion A)              #")
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
        print("# 1. Leer nombre (subOpcion B)                 #")
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
