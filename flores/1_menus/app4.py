import libreria


# Aplicacion para guardar datos de pedir productos

def agregarProducto():
    # 1. Pedir productos
    # 2. Pedir precio
    # 3. Guardar los datos en el archivo 4_app.txt
    producto= libreria.pedir_producto("Ingrese producto : ")
    precio= libreria.pedir_precio("Ingrese precio : ")
    contenido= producto +"-"+str(precio)+"\n"
    libreria.guardar_datos("4_app.txt", contenido, "a")
    print("Datos guardados")

def leerProductos():
    print("Producto       Precio")
    datos= libreria.obtener_datos_lista("4_app.txt")
    for linea in datos:
        linea=linea.replace("\n","")
        producto,precio,=linea.split("-")
        print(producto + "       -     "+precio)
    print(" Datos leidos")


opc=0
max=3
while ( opc != max ):
    print("##################################################")
    print("############  MENU ###############################")
    print("##################################################")
    print("# 1. Pedir producto y precio                     #")
    print("# 2. Leer producto y precio                      #")
    print("# 3. Salir                                       #")
    print("##################################################")

    opc = libreria.pedir_numero("Ingrese opcion : ", 1, 3)

    if ( opc == 1 ):
        agregarProducto()

    if ( opc == 2):
        leerProductos()
# fin_menu

print("Fin del programa")
