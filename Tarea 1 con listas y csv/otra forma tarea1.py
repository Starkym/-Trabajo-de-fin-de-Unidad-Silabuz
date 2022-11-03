import os
import time
import csv


""" Tarea 1
Se tiene la clase Libro con los siguientes atributos: id, título, género, ISBN, autorl y autor(es). Considerar que un libro puede tener varios autores.
Se solicita escribir un programa en Python que permita registrar libros. Debe utilizar: colecciones (listas, tuplas, etc), funciones y clases de Python.
Dicho programa debe tener un menu (a interactuar en la línea de comando) para:
Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.
Opción 2: Listar libros.
Opción 3: Agregar libro.
Opción 4: Eliminar libro.
Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.
Opción 6: Ordenar libros por título.
Opción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.
Opción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.
Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).
Opción 10: Guardar libros en archivo de disco duro (.txt o csv).
Nota: listar libros involucra: título, género, ISBN, editorial y autor(es) """



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

libros=[] # para corregir
f= open("Registros Libros.csv","a")
#f.write("ID, Título, Género, ISBN, Editorial, Autor(es)")

def archivocsv(data):
    with open("Registros Libros.csv",'a', newline='') as ar:
        writer=csv.writer(ar)
        writer.writerow(data)
        

def listar_libros():
    print('[ID, Título, Género, ISBN, Editorial, Autor(es)]')
    with open("Registros Libros.csv",'r') as ar:
        reader = csv.reader(ar)
        #next(reader)
        for row in reader:
            #if row in list
            print(row)

def crear_registro_libro():
    with open("Registros Libros.csv",'r') as ar:
        reader = csv.reader(ar)
        #next(reader)
        count=0
        for row in reader:
            count +=1
    libronuevo=[]
    print('CREAR REGISTRO DE LIBRO')
    print('*' * 50)
    id = count+1
    titulo = input('Insertar titulo del libro: ').title()
    genero = input('Insertar genero del libro: ').title()
    ISBN = input('Insertar código ISBN: ').title()
    editorial = input('Insertar editorial: ').title()
    autores = input('Insertar autor(es): ').title()

    libro = Libro(id, titulo, genero, ISBN, editorial, autores)

    libronuevo.append(libro.get_id())
    libronuevo.append(libro.get_titulo())
    libronuevo.append(libro.get_genero())
    libronuevo.append(libro.get_ISBN())
    libronuevo.append(libro.get_editorial())
    libronuevo.append(libro.get_autores())


    #print(libronuevo) #
    #libros.append(libronuevo) #
    #print(libros) #
    print("Se agregó el libro de forma correcta.")
    archivocsv(libronuevo)

"""
def elimirar_registro_libro():
    #listar_libros()
    list=[]
    numid=input('Introduce el id del contacto que quieres eliminar: ')
    with open("Registros Libros.csv",'r') as ar:
        reader = csv.reader(ar)
        #next(reader)
        for row in reader:
            if row[0]==str(numid):
                reader.remove(row)
            """ """
            list.append(row)
            #print(type(row[0]))
            for i in list:
                for j in i:
                    if j[0]==str(numid):
                        list.remove(i)
            """ """
        print(list)
"""
           



def run():

    print_options()
    command = input("Selecciona una opción:  ")

    if command == '1':
        pass
    elif command == '2':
        listar_libros()
        #pass
    elif command == '3':
        crear_registro_libro()
    elif command == '4':
        #elimirar_registro_libro()
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
    