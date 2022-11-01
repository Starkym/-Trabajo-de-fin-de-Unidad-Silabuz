import os
import time

#Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
print(RED+"------------------PROYECTO 1-----------------")
print(MAGENTA+"INGRESE LA SOLICITUD REFERENTE A SU NUMERO DE REFERENCIA")
#Print opciones
def print_options():
    print(BLUE+"----------------- CRUD LIBROS ---------------"+RESET)
    print(YELLOW+'[1] Leer archivo txt o csv (max 3)')
    print(MAGENTA+'[2] Listar libros')
    print(RED+'[3] Agregar Libro')
    print(CYAN+'[4] Eliminar Libro')
    print(WHITE+'[5] Buscar por ISBN o titulo')
    print(GREEN+'[6] Ordenar libros por titulo')
    print(BLUE+'[7] Buscar por autor, editorial o genero')
    print(YELLOW+'[8] Buscar por numero de autores')
    print(RED+'[9] Editar o actualizar libro')
    print(MAGENTA+'[10] Guardar libro en archivo txt o csv')
    print(CYAN+'[11] Salir'+RESET)
    print("-" * 20)

#Metodo opciones
def run():

    print_options()
    command = input("Selecciona una opción:  ")

    if command == '1':
        pass
    elif command == '2':
        pass
    elif command == '3':
        pass
    elif command == '4':
        pass
    elif command == '5':
        pass
    elif command == '6':
        pass
    elif command == '7':
        pass
    elif command == '8':
        pass
    elif command == '9':
        pass
    elif command == '10':
        pass
    elif command == '11':
        os._exit(1)

    else:
        print('Opcion inválida, ingrese un numero del 1 al 10')
        time.sleep(2)
        run()

if __name__ == "__main__":
    run()


#Clase libro
class Libro:
    def __init__(self,id:int,titulo:str,genero:str,ISBN: int,editorial:str,autores:str) -> None:
        self.__id=id
        self.__titulo=titulo
        self.__genero=genero
        self.__ISBN=ISBN
        self.__editorial=editorial
        self.__autores=autores
