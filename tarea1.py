import os
import time
import csv


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

class Libro:
    def __init__(self, id, titulo, genero, ISBN, editorial, autores):
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__ISBN = ISBN
        self.__editorial = editorial
        self.__autores = autores

    def get_id(self):
        return self.__id

    def set_id(self, id:int):
        self.__id = id


    def get_titulo(self):
        return self.__titulo


    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero:str):
        self.__genero = genero

    def get_ISBN(self):
        return self.__ISBN

    def set_ISBN(self, ISBN:str):
        self.__ISBN = ISBN

    def get_editorial(self):
        return self.__editorial

    def set_editorial(self, editorial:str):
        self.__editorial = editorial

    def get_autores(self):
        return self.__autores

    def set_autores(self, autores:str):
        self.__autores = autores
























def run():

    print_options()
    command = input("Selecciona una opción:  ")

    if command == '1':
        pass
    elif command == '2':
        listar_libros()
    elif command == '3':
        crear_registro_libro()
    elif command == '4':
        pass
    elif command == '5':
        #buscar_libro_isbn()
    elif command == '6':
        #ordenar_libros()
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
