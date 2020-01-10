import libreria

# Aplicacion para pedir nombre, edad, sexo de las personas en general

def subOpcionA():
    # 1. Pedir nombre
    # 2. Pedir edad (0-100)
    # 3. Pedir sexo
    # 4. Guardar datos en archivo 10_app.txt
    nombre=libreria.pedir_nombre("Ingrese nombre : ")
    edad=libreria.pedir_numero("Ingrese edad : ",0,100)
    sexo=libreria.pedir_sexo("Ingrese sexo : ")
    contenido=nombre+"-"+str(edad)+"-"+sexo+"\n"
    libreria.guardar_datos("10_app.txt", contenido,"a")
    print("Nombre01 agregado")

def subOpcionB():
    print("NOMBRE   EDAD        SEXO")
    informacion=libreria.obtener_datos_lista("10_app.txt")
    for linea in informacion:
        linea=linea.replace("\n","")
        nombre,edad,sexo=linea.split("-")
        print(nombre+ "  -  "+ edad+"  -  "+sexo)
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

