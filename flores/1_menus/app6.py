import libreria


# Aplicacion para guardar datos de nombre de la persona y del dia de la semana

def agregarNombres():
    # 1. Pedir nombre
    # 2. Pedir nombre dell dia de la semana
    # 3. Guardar los datos en el archivo 6_app.txt
    nombre= libreria.pedir_nombre("Ingrese nombre : ")
    dia= libreria.pedir_dia_semana("Ingrese dia de la semana : ")
    contenido= nombre +"-"+dia+"\n"
    libreria.guardar_datos("6_app.txt", contenido, "a")
    print("Datos guardados")

def leerNombres():
    print("Nombre       Dia de semana")
    datos= libreria.obtener_datos_lista("6_app.txt")
    for linea in datos:
        linea=linea.replace("\n","")
        nombre,dia=linea.split("-")
        print(nombre + "       -     "+dia)
    print(" Datos leidos")


opc=0
max=3
while ( opc != max ):
    print("##################################################")
    print("############  MENU ###############################")
    print("##################################################")
    print("# 1. Pedir nombre y dia de la semana             #")
    print("# 2. Listar nomnre y dia de la semana            #")
    print("# 3. Salir                                       #")
    print("##################################################")

    opc = libreria.pedir_numero("Ingrese opcion : ", 1, 3)

    if ( opc == 1 ):
        agregarNombres()

    if ( opc == 2):
        leerNombres()
# fin_menu

print("Fin del programa")

