import libreria


# Aplicacion para guardar datos de pedir cantidad de productos

def agregarProductos():
    # 1. Pedir productos
    # 2. Pedir cantidad
    # 3. Guardar los datos en el archivo 5_app.txt
    producto= libreria.pedir_producto("Ingrese producto : ")
    cantidad= libreria.pedir_kilogramo("Ingrese cantidad : ")
    contenido= producto +"     -     "+str(cantidad)+" kg\n"
    libreria.guardar_datos("5_app.txt", contenido, "a")
    print("Datos guardados")

def leerProductos():
    print("Producto       Precio")
    datos= libreria.obtener_datos("5_app.txt")
    if(datos != ""):
        print(datos)
    else:
        print("Datos no guardados")

opc=0
max=3
while ( opc != max ):
    print("##################################################")
    print("############  MENU ###############################")
    print("##################################################")
    print("# 1. Pedir producto y cantidad                   #")
    print("# 2. Leer producto y cantidad                    #")
    print("# 3. Salir                                       #")
    print("##################################################")

    opc = libreria.pedir_numero("Ingrese opcion : ", 1, 3)

    if ( opc == 1 ):
        agregarProductos()

    if ( opc == 2):
        leerProductos()
# fin_menu

print("Fin del programa")
