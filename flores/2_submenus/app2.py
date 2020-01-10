import libreria

# Aplicacion para pedir nombres y sexo

def subOpcionA():
    # 1. Pedir nombre
    # 2. Pedir sexo
    # 3. Guardar datos en archivo 2_app.txt
    nombre=libreria.pedir_nombre("Ingrese nombre : ")
    sexo=libreria.pedir_sexo("Ingrese sexo : ")
    contenido=nombre+"-"+sexo+"\n"
    libreria.guardar_datos("2_app.txt", contenido,"a")
    print("Datos agregado")

def subOpcionB():
    print("NOMBRE    SEXO")
    sexos=libreria.obtener_datos_lista("2_app.txt")
    for linea in sexos:
        linea=linea.replace("\n","")
        nombre,sexo=linea.split("-")
        print(nombre+ "  -  "+ sexo)
    print("Datos leidos")

def submenu1():
    opc=0
    max=2

    while ( opc != max ):
        print("################################################")
        print("##################  SUBMENU ####################")
        print("################################################")
        print("# 1. Agregar nombre y sexo (subOpcion A)       #")
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
        print("# 1. Leer nombre y sexo  (subOpcion B)         #")
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

