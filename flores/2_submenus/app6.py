import libreria

# Aplicacion para pedir nombre y dni

def subOpcionA():
    # 1. Pedir nombre
    # 2. Pedir dni
    # 3. Guardar datos en archivo 6_app.txt
    nombre=libreria.pedir_nombre("Ingrese nombre : ")
    dni=libreria.pedir_dni("Ingrese dni : ")
    contenido=nombre+"-"+dni+"\n"
    libreria.guardar_datos("6_app.txt", contenido,"a")
    print("Datos agregados")

def subOpcionB():
    print("NOMBRE    DNI")
    nombre_dni=libreria.obtener_datos_lista("6_app.txt")
    for linea in nombre_dni:
        linea=linea.replace("\n","")
        nombre,dni=linea.split("-")
        print(nombre+ "  -  "+ dni)
    print("Datos leidos")

def submenu1():
    opc=0
    max=2

    while ( opc != max ):
        print("################################################")
        print("##################  SUBMENU ####################")
        print("################################################")
        print("# 1. Agregar nombre-dni (subOpcion A)          #")
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
        print("# 1. Leer nombre-dni (subOpcion B)             #")
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

