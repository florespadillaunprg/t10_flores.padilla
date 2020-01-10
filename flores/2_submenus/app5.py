import libreria

# Aplicacion para pedir productos y su informacion de ellos ( precio ) y la cantidad

def subOpcionA():
    # 1. Pedir productos
    # 2. Pedir cantidad
    # 3. Pedir precio
    # 4. Guardar datos en archivo 1_app.txt
    producto=libreria.pedir_producto("Ingrese producto : ")
    cantidad=libreria.pedir_kilogramo("Ingrese cantidad : ")
    precio=libreria.pedir_precio("Ingrese precio : ")
    contenido=producto+"-"+str(cantidad)+" kg -"+str(precio)+"\n"
    libreria.guardar_datos("5_app.txt", contenido,"a")
    print("Datos agregados")

def subOpcionB():
    print("NOMBRE   CANTIDAD   PRECIO")
    productos=libreria.obtener_datos_lista("5_app.txt")
    for linea in productos:
        linea=linea.replace("\n","")
        producto,cantidad,precio=linea.split("-")
        print(producto+"  -  "+cantidad+"  -  "+precio)
    print("Datos leidos")

def submenu1():
    opc=0
    max=2

    while ( opc != max ):
        print("################################################")
        print("##################  SUBMENU ####################")
        print("################################################")
        print("# 1. Agregar productos (subOpcion A)           #")
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
        print("# 1. Leer productos (subOpcion B)              #")
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

