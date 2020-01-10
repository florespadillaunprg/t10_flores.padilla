import libreria

# Aplicacion para pedir nombres y apellidos completos

def subOpcionA():
    # 1. Pedir nombre01
    # 2. Pedir nombre02
    # 3. Pedir apellido01
    # 4. Pedir apellido02
    # 5. Guardar datos en archivo 4_app.txt
    nombre01=libreria.pedir_nombre("Ingrese nombre01 : ")
    nombre02=libreria.pedir_nombre("Ingrese nombre02 : ")
    apellido01=libreria.pedir_nombre("Ingrese apellido 01 : ")
    apellido02=libreria.pedir_nombre("Ingrese apellido 02 : ")
    contenido=nombre01+"-"+nombre02+"-"+apellido01+"-"+apellido02+"\n"
    libreria.guardar_datos("4_app.txt", contenido,"a")
    print("Datos agregados")

def subOpcionB():
    print("NOMBRE01   NOMBRE02   APELLIDO01   APELLIDO02")
    nombre_completo=libreria.obtener_datos_lista("4_app.txt")
    for linea in nombre_completo:
        linea=linea.replace("\n","")
        nombre01,nombre02,apellido01,apellido02=linea.split("-")
        print(nombre01+"  -  "+nombre02+"  -  "+apellido01+"  -  "+apellido02)
    print("Datos leidos")

def submenu1():
    opc=0
    max=2

    while ( opc != max ):
        print("################################################")
        print("##################  SUBMENU ####################")
        print("################################################")
        print("# 1. Agregar nombre completo (subOpcion A)     #")
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
        print("# 1. Leer nombre completo (subOpcion B)        #")
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

