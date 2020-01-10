import libreria

# Aplicacion para guardar datos del sexo de las personas

def agregarSexo():
    # 1. Pedir nombres
    # 2. Pedir sexo
    # 3. Guardar los datos en el archivo 9_app.txt
    nombre= libreria.pedir_nombre("Ingrese nombre : ")
    sexo= libreria.pedir_sexo("Ingrese sexo : ")
    contenido= nombre +"-"+sexo+"\n"
    libreria.guardar_datos("9_app.txt", contenido, "a")
    print("Datos guardados")

def leerSexo():
    print("Nombre       Sexo")
    datos= libreria.obtener_datos_lista("9_app.txt")
    for linea in datos:
        linea=linea.replace("\n","")
        nombre,sexo=linea.split("-")
        print(nombre + "       -     "+sexo)
    print(" Datos leidos")


opc=0
max=3
while ( opc != max ):
    print("##################################################")
    print("############  MENU ###############################")
    print("##################################################")
    print("# 1. Pedir nombre y sexo                         #")
    print("# 2. Listar nomnre y sexo                        #")
    print("# 3. Salir                                       #")
    print("##################################################")

    opc = libreria.pedir_numero("Ingrese opcion : ", 1, 3)

    if ( opc == 1 ):
        agregarSexo()

    if ( opc == 2):
        leerSexo()
# fin_menu

print("Fin del programa")


