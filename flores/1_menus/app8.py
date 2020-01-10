import libreria


# Aplicacion para guardar datos de del mes y del anio

def agregarMes():
    # 1. Pedir nombre del mes
    # 2. Pedir anio
    # 3. Guardar los datos en el archivo 8_app.txt
    mes= libreria.pedir_mes("Ingrese mes : ")
    anio= libreria.pedir_anio("Ingrese anio : ")
    contenido= mes +"-"+str(anio)+"\n"
    libreria.guardar_datos("8_app.txt", contenido, "a")
    print("Datos guardados")

def leerMes():
    print("Mes               Anio")
    datos= libreria.obtener_datos_lista("8_app.txt")
    for linea in datos:
        linea=linea.replace("\n","")
        mes,anio=linea.split("-")
        print(mes + "     -        "+anio)
    print("Datos leidos")



opc=0
max=3
while ( opc != max ):
    print("##################################################")
    print("############  MENU ###############################")
    print("##################################################")
    print("# 1. Pedir mes y anio                            #")
    print("# 2. Listar mes y anio                           #")
    print("# 3. Salir                                       #")
    print("##################################################")

    opc = libreria.pedir_numero("Ingrese opcion : ", 1, 3)

    if ( opc == 1 ):
        agregarMes()

    if ( opc == 2):
        leerMes()
# fin_menu

print("Fin del programa")

