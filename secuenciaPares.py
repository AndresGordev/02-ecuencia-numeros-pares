""" Programa que, mediante un numero entero inicial y un numero entero
final, se genera una secuencia de numeros pares""" 

#-------------Bloque de todos loa mensajes que el programa mostrara ----
def encabezado():
    print("*" * 64)
    print("    Numeros pares en la secuencia de numeros de tu eleccion     ")
    print("*" * 64)

def numero_inicial():
    return input("Ingresa un numero entero inicial, entre el 1 y el 100: ")   

def numero_final(numero_inicial):
    return input(f"Ingresa un numero entero final entre el {numero_inicial +1} y el 100: ")

def mensaje_campo_vacio():
    print("No debes dejar el campo vacio. Intentalo de nuevo...\n")

def mensaje_no_numero():
    print("Debes ingresar solo numeros enteros. Intentalo de nuevo...\n")

def mensaje_numero_no_valido():
    print("Debes ingresar un numero entre el 1 y el 100. Intentalo de nuevo...\n")

def mensaje_numero_incorrecto_final(numero_inicial):
    print(f"El numero final debe ser mayor a {numero_inicial}")

def mensaje_numero_incorrecto_inicial():
    print(f"El numero inicial debe ser menor que 100. Intentalo de nuevo...\n")

def mensaje_secuencia_generada(numero_inicial, numero_final):
    print(f"***** Secuencia de numeros pares del {numero_inicial} al {numero_final}: *****")
#-------------------------------------------------------------------

#-------------------Bloque de los separadores del programa----------
def espacio():
    print("\n")

def separacion():
    print("-" * 60)
    espacio()
#-------------------------------------------------------------------
#--------------------Bloque de funciones independientes-------------
#Función que verifica si el usuario deja el campo solicitado vacio.
#Se utiliza .strip para quitar espacios, asi como saltos de linea.
def campo_vacio(numero):
    if numero.strip() == "":
        return True
#Funcion que verifica si el dato ingresado es un digito y no un caracter o letra.
def no_numero(numero):
    if numero.isdigit():
        return True
#Función que verifica si el numero ingresado es congruente con lo indicado.
def numero_valido(numero):
    if int(numero) < 1 or int(numero) > 100:
        return True
#Función que verifica si el numero inicial cumple lo solicitado para que...
#se pueda generar una secuencia correcta.
#Se devuelve un valor booleano en el caso de ser asi.
def mayor_que_cien(numero_inicial):
    if int(numero_inicial) >= 100:
        return True
#Función que devuelve un valor booleano verdadero...
#si la comparacion entre los dos numeros solicitados anteriormente se cumple.
def numero_incorrecto_final(numero_inicial,numero_final):
    if int(numero_final) <= int(numero_inicial):
        return True
    
#---------------Bloque de verificaciones iniciales--------------------------

# Para el numero inicial y numero final, se realizan las siguientes verificaciones:
# si el usuario deja el campo solicitado vacio, se le notifica y mediante un bucle while...
# se le vuelve a pedir el dato requerido hasta que lo ingrese de manera correcta.
# Cuando el usuario ingrese un numero, se sale del bucle y se devuelve el mismo para posteriores verificaciones.
def verificacion_campo_numero_inicial():
    incorrecto = True
    while incorrecto:
        numero_inicial_devuelto = numero_inicial()
        if campo_vacio(numero_inicial_devuelto):
            mensaje_campo_vacio()
        else:
            incorrecto = False
    return numero_inicial_devuelto

def verificacion_campo_numero_final():
    incorrecto = True
    while incorrecto:
        numero_final_devuelto = numero_final(numero_inicial)
        if campo_vacio(numero_final_devuelto):
            mensaje_campo_vacio()
        else:
            incorrecto = False
    return numero_final_devuelto
#---------------------------------------------------------------------------------

#-----------------------------Bloque de verificaciones completas------------------

# Para el numero inicial y final se realizan las siguientes verificaciones:
# Con el numero devuelto en las verificaciones iniciales anteriores, asi como con las funciones de verificacion previamente creadas...
# Se verifica, si el numero inicial es mayor que 100, se le notifica al usuario y a traves del bucle while, se lo vuelve a solicitar.
# Se verifica, si el numero inicial o final que ingreso el usuario sea un digito y no un caracter o letra.
# Se verifica, si el numero inicial o final que ingresó el usuario esta dentro del rango solicitado.
# Si el numero ingresado por el usuario pasa todas las verificaciones, entonces se sale del bucle y se devuelve como entero para proximos procesos.

def verificacion_total_numero_inicial():
    incorrecto = True

    while incorrecto: 
        numero_inicial = verificacion_campo_numero_inicial()
        if mayor_que_cien(numero_inicial):
            mensaje_numero_incorrecto_inicial()
        elif not no_numero(numero_inicial):
            mensaje_no_numero()
        elif numero_valido(numero_inicial):
            mensaje_numero_no_valido()
        else:
            espacio()
            incorrecto = False
    return int(numero_inicial)

# Con el numero devuelto de la verificacion anterior, se realiza las siguientes verificaciones:
# Se verifica, si el numero final es mayor que el numero inicial, de lo contrario, se le alerta al usuario y se le vuelve a solicitar.
# Se verifica, si el numero final ingresado es un digito y no un caracter o letra.
# Se verifica, si el numero final es congruente con el rango solicitado.
# Si el numero ingresado cumple con todas las inidicaciones, se sale del bucle y se devuelve como entero para proximos procesos.
def verificacion_total_numero_final(numero_inicial):
    incorrecto = True

    while incorrecto:
        numero_final = verificacion_campo_numero_final()
        if numero_incorrecto_final(numero_inicial,numero_final):
            mensaje_numero_incorrecto_final(numero_inicial)
        elif not no_numero(numero_final):
            mensaje_no_numero()
        elif numero_valido(numero_final):
            mensaje_numero_no_valido()
        else:
            espacio()
            incorrecto = False
    return int(numero_final)
#-----------------------------------------------------------------------------------------

#------------------------------Bloque generador de la secuencia------------------------------

# Mediante un bucle for, se agrega el numero iterado en el rango del numero inicial y el numero final...
# a la lista que se declara previamente.
# Una vez terminando la iteracion, se muestra el mensaje de "Secuencia generada" entre el numero inicial y el numero final.
# Se muestra la secuencia de numeros pares generada, separada por un guion.

def generador_secuencia(numero_inicial, numero_final):
    secuencia = []
    for numero in range(numero_inicial, numero_final +1):
        if numero % 2 ==0:
            secuencia.append(numero)
    mensaje_secuencia_generada(numero_inicial, numero_final)
    espacio()
    print(*secuencia, sep=("-"))
#--------------------------------------------------------------------------------------------

#------------------------------Bloque de logica principal------------------------------------

# Se muestra el encabezado y hace el llamado a la funcion que verifica al numero inicial.
# Se hace el llamado a la funcion que verifica al numero final
# Por ultimo, se hace el llamado a la funcion que genera a la secuencia de numero pares, a traves de los numeros devueltos con las...
# funiones anteriores; numero inicial y numero final.
encabezado()
espacio()
numero_inicial = verificacion_total_numero_inicial()
numero_final = verificacion_total_numero_final(numero_inicial)
separacion()
generador_secuencia(numero_inicial, numero_final)