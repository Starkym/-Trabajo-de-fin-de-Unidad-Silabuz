import os
import time

#Colores
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[39m'

#Print opciones
def print_options():
    print(BLUE+"----------------- CRUD LIBROS ---------------"+RESET)
    print(YELLOW+'[1] Leer archivo txt o csv (max 3)')
    print('[2] Listar libros')
    print('[3] Agregar Libro')
    print('[4] Eliminar Libro')
    print('[5] Buscar por ISBN o titulo')
    print('[6] Ordenar libros por titulo')
    print('[7] Buscar por autor, editorial o genero')
    print('[8] Buscar por numero de autores')
    print('[9] Editar o actualizar libro')
    print('[10] Guardar libro en archivo txt o csv')
    print('[11] Salir'+RESET)
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
