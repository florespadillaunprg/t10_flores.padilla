import libreria


# Aplicacion para guardar datos de el dia de la semana con su respectiva fecha

def agregarSemana():
    # 1. Pedir nombre del dia de la semana
    # 2. Pedir dia
    # 3. Guardar los datos en el archivo 7_app.txt
    dia_semana= libreria.pedir_dia_semana("Ingrese dia de la semana : ")
    dia= libreria.pedir_dia("Ingrese dia : ")
    contenido= dia_semana +"-"+str(dia)+"\n"
    libreria.guardar_datos("7_app.txt", contenido, "a")
    print("Datos guardados")

def leerSemana():
    print("Dia de la semana       Dia ")
    datos= libreria.obtener_datos_lista("7_app.txt")
    for linea in datos:
        linea=linea.replace("\n","")
        dia_semana,dia=linea.split("-")
        print(dia_semana + "          -        "+dia)
    print(" Datos leidos")


opc=0
max=3
while ( opc != max ):
    print("##################################################")
    print("############  MENU ###############################")
    print("##################################################")
    print("# 1. Pedir nombre del dia de la semana           #")
    print("# 2. Listar nombre del dia de la semana          #")
    print("# 3. Salir                                       #")
    print("##################################################")

    opc = libreria.pedir_numero("Ingrese opcion : ", 1, 3)

    if ( opc == 1 ):
        agregarSemana()

    if ( opc == 2):
        leerSemana()
# fin_menu

print("Fin del programa")

