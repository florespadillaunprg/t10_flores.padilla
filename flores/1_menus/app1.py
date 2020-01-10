import libreria

# Aplicacion para guardar datos de los estudiantes

def agregarEstudiante():
    # 1. Pedir nombre del estudiante
    # 2. Pedir la nota del estudiante (0-20)
    # 3. Guardar los datos en el archivo 1_app.txt
    nombre = libreria.pedir_nombre("Ingrese Nombre:")
    nota = libreria.pedir_numero("Ingrese Nota:", 0, 20)
    contenido=nombre + " tiene nota " + str(nota) + "\n"
    libreria.guardar_datos("1_app.txt", contenido, "a")
    print("Datos del estudiante guardados")

def mostrarEstudiante():
    notas = libreria.obtener_datos("1_app.txt")
    if ( notas != ""):
        print(notas)
    else:
        print("Datos del estudiante no guardados")

opc=0
max=3
while(opc != max):
    print("############################################")
    print("################### MENU ###################")
    print("############################################")
    print("#    1. Agregar Esudiante                  #")
    print("#    2. Mostrar Estudiante                 #")
    print("#    3. Salir                              #")
    print("############################################")

    opc= libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        agregarEstudiante()
    if (opc == 2):
        mostrarEstudiante()

#fin_menu
print("Fin del programa")
