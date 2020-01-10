def validar_entero(n):
    if (isinstance(n, int)):
        return True
    else:
        return False

def validar_rango(n, ri, rf):
    if ( validar_entero(n) == True):
        if (n >= ri and n <= rf):
            return True
        else:
            return False
    else:
        return False

def pedir_numero(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
#fin_pedir_numero

def validar_nombre(nombre):
    if ( isinstance(nombre, str)):
        if (len(nombre) >= 3):
            return True
        else:
            return False
    else:
        return False

def pedir_nombre(msg):
    nombre=""
    while ( validar_nombre(nombre) == False ):
        nombre=input(msg)
    #fin_while
    return nombre
#fin_pedir_nombre

def guardar_datos(nombre_archivo, contenido, modo):
    archivo=open(nombre_archivo, modo)
    archivo.write(contenido)
    archivo.close()

def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido = archivo.read()
    archivo.close()
    return contenido

def obtener_datos_lista(nombre_archivo):
    archivo=open(nombre_archivo)
    lista = archivo.readlines()
    archivo.close()
    return lista


def validar_byte(byte):
    # 1. Ocupa 8 caracteres
    if ( len(byte) != 8):
        return False

    # 2. La cadena debe ser digitos
    if ( byte.isdigit() == False ):
        return False

    # 3. Cada caracter debe ser 0 o 1
    for bit in byte:
        if ( bit != "0" and bit != "1" ):
            return False
        #fin_if
    #fin_for

    # Si llego hasta aqui, es porque es un Byte correcto
    return True
#fin_validar_byte

def pedir_byte(msg):
    byte=""
    while( validar_byte(byte) == False):
        byte=input(msg)
    return byte
#fin_pedir_byte

def mascara(bit1, bit2):
    if ( bit1 == "1" and bit2 == "1" ):
        return "1"
    else:
        return "0"

def enmascarar(byte1, byte2):
    mask=""
    for i in range(8):
        mask += mascara(byte1[i], byte2[i])
    #fin_for
    return mask
def validar_continente(msg):
    if ( isinstance(msg,str)):
        if(msg=="america" and msg=="africa" and msg=="europa" and msg=="asia" and msg=="oceania"):
            return True
    else:
        return False

def pedir_continente(msg):
    continente=""
    while(validar_continente(continente)==False):
        continente=input(msg)
    return continente

def validar_sexo(msg):
    if(isinstance(msg,str)):
        if(msg=="masculino" and msg=="femenino"):
            return True
    else:
        return False

def pedir_sexo(msg):
    sexo=""
    while(validar_sexo(sexo)==False):
        sexo=input(msg)

    return sexo

def validar_operador(msg):
    if(isinstance(msg,str)):
        if(msg=="sumando" and msg=="sustraendo" and
            msg=="multiplicador" and msg=="divisor"):
                return True

        else: False
    else:
        return False


def pedir_operador(msg):
    opera=""
    while(validar_operador(opera)==False):
        opera=input(msg)

    return opera


def validar_universidad(msg):
    if(isinstance(msg,str)):
        if(msg=="UNPRG" or msg=="UDCH" or msg=="USS" or msg=="UCV" ):
            return True
        else:
            return False


    else:
        return False


def pedir_universidad(msg):
    universidad=""
    while(validar_universidad(universidad)==False):
        universidad=input(msg)

    return universidad


def validar_colegio(msg):
    if(isinstance(msg,str)):
        if(msg=="Basadre" or msg=="Cima" or msg=="Gajel" or msg=="San Jose" ):
            return True
        else:
            return False


    else:
        return False


def pedir_colegio(msg):
    colegio=""
    while(validar_colegio(colegio)==False):
        colegio=input(msg)

    return colegio


def validar_marca(msg):
    if(isinstance(msg,str)):
        if(msg=="LG" or msg=="HP" or msg=="SAMSUNG" or msg=="LENOVO" ):
            return True
        else:
            return False


    else:
        return False


def pedir_marca(msg):
    marca=""
    while(validar_marca(marca)==False):
        marca=input(msg)

    return marca

def validar_memoria(msg):
    if(isinstance(msg,str)):
        if(msg=="8GB" or msg=="16 GB" or msg=="32GB" or msg=="64GB" ):
            return True
        else:
            return False


    else:
        return False


def pedir_memoria(msg):
    memoria=""
    while(validar_memoria(memoria)==False):
        memoria=input(msg)

    return memoria
