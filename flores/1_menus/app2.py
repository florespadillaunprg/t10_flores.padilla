import libreria


# Aplicacion para guardar datos de los trabajadores

def agregarTrabajador():
    # 1. Pedir nombre del trabajador
    # 2. Pedir la edad del trabajador (1-100)
    # 3. Guardar los datos en el archivo 2_app.txt
    nombre = libreria.pedir_nombre("Ingrese Nombre:")
    edad = libreria.pedir_numero("Ingrese Edad:", 1, 100)
    contenido=nombre + " tiene " + str(edad) + " anios "+ "\n"
    libreria.guardar_datos("2_app.txt", contenido, "a")
    print("Datos del trabajador guardados")

def leerTrabajador():
    informacion = libreria.obtener_datos("2_app.txt")
    if ( informacion != ""):
        print(informacion)
    else:
        print("Archivo sin datos")

opc=0
max=3
while(opc != max):
    print("############################################")
    print("################### MENU ###################")
    print("############################################")
    print("#    1. Agregar Trabajador                 #")
    print("#    2. Leer Trabajador                    #")
    print("#    3. Salir                              #")
    print("############################################")

    opc= libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        agregarTrabajador()
    if (opc == 2):
        leerTrabajador()

#fin_menu
print("Fin del programa")
