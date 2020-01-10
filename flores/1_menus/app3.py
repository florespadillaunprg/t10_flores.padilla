import libreria


# Aplicacion para guardar datos de los pacientes

def agregarPaciente():
    # 1. Pedir nombre del paciente
    # 2. Pedir la edad del paciente (32-39)
    # 3. Guardar los datos en el archivo 3_app.txt
    nombre = libreria.pedir_nombre("Ingrese Nombre:")
    temperatura = libreria.pedir_numero("Ingrese Temperatura:", 32, 39)
    contenido=nombre + " tiene " + str(temperatura) +"° de temperatura "+ "\n"
    libreria.guardar_datos("3_app.txt", contenido, "a")
    print("Datos del paciente guardados")

def leerPaciente():
    informacion = libreria.obtener_datos("3_app.txt")
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
    print("#    1. Agregar Temperatura                #")
    print("#    2. Leer Temperatura                   #")
    print("#    3. Salir                              #")
    print("############################################")

    opc= libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        agregarPaciente()

    if (opc == 2):
        leerPaciente()

#fin_menu
print("Fin del programa")
