# validar entero
def validar_entero(n):
    if (isinstance(n, int)):
        return True
    else:
        return False
# fin_validar_entero

# validar rango
def validar_rango(n, ri, rf):
    if ( validar_entero(n) == True):
        if (n >= ri and n <= rf):
            return True
        else:
            return False
    else:
        return False
# fin_validar_rango

# pedir numero
def pedir_numero(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
#fin_pedir_numero

# validar nombre
def validar_nombre(nombre):
    if ( isinstance(nombre, str)):
        if (len(nombre) >= 3):
            return True
        else:
            return False
    else:
        return False
# fin_validar_nombre

# pedir nombre
def pedir_nombre(msg):
    nombre=""
    while ( validar_nombre(nombre) == False ):
        nombre=input(msg)
    #fin_while
    return nombre
#fin_pedir_nombre

# guardas datos
def guardar_datos(nombre_archivo, contenido, modo):
    archivo=open(nombre_archivo, modo)
    archivo.write(contenido)
    archivo.close()
# fin_guardar datos

# obtener_datos
def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido = archivo.read()
    archivo.close()
    return contenido
# fin_obtener_datos

# obtener datos lista
def obtener_datos_lista(nombre_archivo):
    archivo=open(nombre_archivo)
    lista = archivo.readlines()
    archivo.close()
    return lista
# fin obtener_Datos_lista

# validar producto
def validar_producto(producto):
    if (isinstance(producto,str)):
        if ( len(producto) >= 3):
            return True
        else:
            return False
    else:
        return False
# fin validar_producto

# pedir_producto
def pedir_producto(msg):
    producto=""
    while ( validar_producto(producto) == False ):
        producto=input(msg)
    #fin_while
    return producto
# fin_pedir_producto

# validar_precio
def validar_precio(precio):
    if ( isinstance( precio,float ) or isinstance( precio, int)):
        if ( precio > 0 or precio > 0.0):
            return True
        else:
            return False
    else:
        return False
# fin_validar_precio

# pedir_precio
def pedir_precio(msg):
    precio=""
    while( validar_precio(precio) == False):
       precio=input(msg)
       if ( precio.isdigit() == True):
           precio = int(precio) or float(precio)
    #fin_while
    return precio
# fin_pedir_precio

# validar kilogramo
def validar_kilogramo(kilogramo):
    if ( isinstance(kilogramo,int)):
        if( kilogramo > 0):
            return True
        else:
            return False
    else:
        return False
# fin_validar_kilogramo

# pedir_kilogramo
def pedir_kilogramo(msg):
    kilogramo=""
    while( validar_kilogramo(kilogramo) == False):
       kilogramo=input(msg)
       if ( kilogramo.isdigit() == True):
           kilogramo = int(kilogramo)
    #fin_while
    return kilogramo
# fin_pedir_kilogramo

# validar_dia
def validar_dia(dia):
    if (isinstance(dia,int)):
       if ( dia > 0 and dia <= 30):
           return True
       else:
           return False
    else:
        return False
# fin_validar_dia

# pedir_dia
def pedir_dia(msg):
    dia=""
    while( validar_dia(dia) == False):
       dia=input(msg)
       if ( dia.isdigit() == True):
           dia = int(dia)
    #fin_while
    return dia
# fin_pedir_dia

# validar_mes
def validar_mes(mes):
    if ( isinstance(mes, str)):
        if(mes=="enero" or mes=="febrero" or mes == "marzo" or mes =="abril" or mes =="mayo" or mes == "junio"
        or mes=="julio" or mes=="agosto" or mes=="setiembre" or mes=="octubre" or mes =="noviembre"
        or mes=="diciembre"):
            return True
        else:
            return False
    else:
        return False
# fin_validar_mes

# pedir_mes
def pedir_mes(msg):
    mes=""
    while(validar_mes(mes)==False):
        mes=input(msg)
    # fin_while
    return mes
# fin_pedir_mes

# validar_anio
def validar_anio(anio):
    if(isinstance(anio,int)):
        return True
    else:
        return False
# fin_validar_anio

# pedir_anio
def pedir_anio(msg):
    anio=""
    while( validar_anio(anio) == False):
       anio=input(msg)
       if ( anio.isdigit() == True):
           anio = int(anio)
    #fin_while
    return anio
# fin_pedir_anio

# validar_dia_semana
def validar_dia_semana(dia_semana):
    if ( isinstance(dia_semana,str)):
        if (dia_semana=="lunes" or dia_semana=="martes" or dia_semana=="miercoles" or dia_semana=="jueves"
        or dia_semana=="viernes" or dia_semana=="sabado" or dia_semana=="domingo"):
            return True
        else:
            return False
    else:
        return False
# fin_validar_Dia_semana

# pedir_dia_semana
def pedir_dia_semana(msg):
    dia_semana=""
    while (validar_dia_semana(dia_semana)==False):
        dia_semana=input(msg)
    # fin_while
    return dia_semana
# fin_pedir_dia_semana

# validar_sexo
def validar_sexo(sexo):
    if (isinstance(sexo,str)):
        if(sexo=="m" or sexo=="f" or sexo=="masculino" or sexo =="femenino" or sexo=="M" or sexo=="F"
        or sexo=="MASCULINO" or sexo=="FEMENINO"):
            return True
        else:
            return False
    else:
        return False
# fin_validar_Sexo

# pedir_sexo
def pedir_sexo(msg):
    sexo=""
    while(validar_sexo(sexo)==False):
        sexo=input(msg)
    # fin_while
    return sexo
# fin_pedir_sexo

# validar_dni
def  validar_dni(dni):
    if (isinstance(dni,str)):
        if (len(dni)==8):
            if (dni != 0):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
# fin_validar_dni

# pedir_dni
def pedir_dni(msg):
    dni=""
    while ( validar_dni(dni) == False):
        dni=input(msg)
    # fin_while
    return dni
# fin_pedir_dni
