import libreria


# Aplicacion para guardar datos de nombre de la persona y del mes

def agregarDatos():
    # 1. Pedir nombre
    # 2. Pedir mes
    # 3. Guardar los datos en el archivo 10_nacimiento.txt
    nombre= libreria.pedir_nombre("Ingrese nombre : ")
    mes= libreria.pedir_mes("Ingrese mes : ")
    contenido= nombre +"-"+mes+"\n"
    libreria.guardar_datos("10_app.txt", contenido, "a")
    print("Datos guardados")

def leerDatos():
    print("Nombre       Dia de semana")
    datos= libreria.obtener_datos_lista("10_app.txt")
    for linea in datos:
        linea=linea.replace("\n","")
        nombre,mes=linea.split("-")
        print(nombre + "       -     "+mes)
    print(" Datos leidos")


opc=0
max=3
while ( opc != max ):
    print("##################################################")
    print("############  MENU ###############################")
    print("##################################################")
    print("# 1. Pedir nombre y mes                          #")
    print("# 2. Listar nomnre y mes                         #")
    print("# 3. Salir                                       #")
    print("##################################################")

    opc = libreria.pedir_numero("Ingrese opcion : ", 1, 3)

    if ( opc == 1 ):
        agregarDatos()

    if ( opc == 2):
        leerDatos()
# fin_menu

print("Fin del programa")


