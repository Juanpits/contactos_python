import os

CARPETA = 'contactos/' #Carpeta de contactos
EXTENSION = '.txt' #Extension de los archivos

# Contactos

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    #Revisa si la carpeta existe o no
    crear_directorio()

    #Muestra el menú de opciones
    mostrar_menu()

    #Preguntar al usuario la acción a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción \r\n')
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contacto()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción no válida')


def editar_contacto():
    print('Escribe el contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')

    #Revisar si el archivo ya existe
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            nombre_contacto = input('Agrega el nuevo nombre: \r\n')
            telefono_contacto = input('Agrega el nuevo teléfono: \r\n')
            categoria_contacto = input('Agrega la nueva categoría: \r\n')

            #Instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')

            #Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            #Mensaje de éxito
            print('Contacto editado satisfactoriamente')
    else:
        print('Este contacto no existe')
    #Reiniciar la aplicación
    app()

def agregar_contacto():
    print('Escribe los datos del nuevo Contacto')
    nombre_contacto = input('Nombre del contacto: \r\n')

    #Revisar si el archivo ya existe
    existe = existe_contacto(nombre_contacto)

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            #Resto de datos
            telefono_contacto = input('Agrega el teléfono: \r\n')
            categoria_contacto = input('Agrega la categoría: \r\n')

            #Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')

            #Mostrar un mensaje de éxito
            print('\r\n Contacto creado correctamente \r\n')
    else:
        print('Ese contacto ya existe')
    
    #Reiniciar la app
    app()

def mostrar_contacto():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #Imprime los contenidos
                print(linea.rstrip())
            #Imprime un separador entre contactos
            print('\r\n')

def buscar_contacto():
    nombre = input('Seleccione el Contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del Contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)
    
    #Reiniciar la app
    app()

def eliminar_contacto():
    nombre = input('Seleccione el Contacto que desea eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nEliminado Correctamente')
    except:
        print('No existe ese contacto')
    
    app()

def mostrar_menu():
    print('Seleccione del menú lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contacto')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

def crear_directorio():
    if not os.path.exists(CARPETA): #Si no existe la carpeta
        os.makedirs(CARPETA) #Crea la carpeta

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)





app()