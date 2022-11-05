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

libros=[] # para corregir
f= open("Registros Libros.csv","a")
"""
f1= open("Registros Libros.csv","r")
for linea in f1:
    if len(linea)>0:
        pass
    else:
        f.write("ID, Título, Género, ISBN, Editorial, Autor(es)\n")
        f.close()
"""
def archivocsv(data):
    with open("Registros Libros.csv",'a', newline='') as ar:
        writer=csv.writer(ar)
        writer.writerow(data)
    
def repetir_opciones():
    dato = input("\nRegresar al menu? si o no: ").lower()
    if dato == 'si':
        run()
    else:
        os._exit(0)
        
biblioteca = list()

def listar_libros():
    print('[ID, Título, Género, ISBN, Editorial, Autor(es)]')
    with open("Registros Libros.csv",'r') as ar:
        reader = csv.reader(ar)
        #next(reader)
        for row in reader:
            #if row in list
            print(row)

    repetir_opciones()

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

    repetir_opciones()


#Opcion5
def buscar_libroxisbn():
    print("1) ISBN\n2) Titulo")
    opcion = input("Elige una opcion:  ")

    if opcion == '1':
        isbnx = input('Ingresar el ISBN del libro: ')
        with open("Registros Libros.csv",'r') as ar:
            reader = csv.reader(ar)
            data=[line for line in reader]
            for row in data:
                if row[3]==isbnx:
                    data.append(row)
                    print(f"ISBN: {isbnx}")
                    print("\nLibro:")
                    print(*row)
                    break;
                
    if opcion == '2':
        titulox=input('Ingresar el Titulo del libro: ')
        with open("Registros Libros.csv",'r') as ar:
            reader = csv.reader(ar)
            data=[line for line in reader]
            for row in data:
                if row[1]==titulox:
                    data.append(row)
                    print(f"Titulo: {titulox}")
                    print("\nLibro:")
                    print(*row)
                    break;
                    #print(f"\nTitulo: {titulox}\n")
                    #print(*row)
                    #break;



#Opcion6
def ordenar_libros():
    lista_id = []
    lista_titulo = []
    lista_genero = []
    lista_ISBN = []
    lista_editorial = []
    lista_autores = []
    print(BLUE+"Ordenado por titulo: "+RESET )
    with open("Registros Libros.csv",'r') as ar:
        lista_ordenada = []
        reader = csv.reader(ar)
        for i in reader:
            id,titulo,genero,ISBN,editorial,autores,*a = i
            #lista_id.append(id)
            lista_titulo.append(titulo)
            #lista_genero.append(titulo)
            #lista_ISBN.append(titulo)
            #lista_editorial.append(titulo)
            #lista_autores.append(titulo)
        #comienzo indice1
        #lista_id.pop(0)
        #lista_titulo.pop(0)
        #lista_genero.pop(0)
        #lista_ISBN.pop(0)
        #lista_editorial.pop(0)
        #lista_autores.pop(0)
        #lista_titulo_ordenada
        lista_titulo.sort()

        #agrupacion de listas
        #lista_ordenada = zip(lista_titulo)
        for count,valor in enumerate(zip(lista_titulo), start=1):
            print(count," - ",  *valor)
        #print(f"- {i}") 
            #_, titulo,_,_,*a = i
            #lista_ordenada.append(titulo)
        #lista_ordenada.pop(0)
        #lista_ordenada.sort()
        #print(f"Lista ordenada: {lista_ordenada}")

    repetir_opciones()

def eliminar(self):
    codigo = input("INSERTE EL CODIGO QUE DESEA ELIMINAR :")
    for index in range(len(self.__cod)):
        if codigo == self.__cod[index][0]:
            index_flag = index 
            self.self.__cod = self.self.__cod[:index_flag] + self.self.__cod[index_flag+1:]
            self.self.__code.sort(key=lambda x: x[3]) 
    repetir_opciones()    

def actualizar_libro():
    id2=input('ingresar el ID del libro a actualizar: ')
    with open("Registros Libros.csv",'r') as ar:
        reader = csv.reader(ar)
        data=[line for line in reader]
        for row in data:
            if row[0]==id2:
                data.remove(row)
        titulo = input('Insertar titulo del libro: ').title()
        genero = input('Insertar genero del libro: ').title()
        ISBN = input('Insertar código ISBN: ').title()
        editorial = input('Insertar editorial: ').title()
        autores = input('Insertar autor(es): ').title()
        libronuevo=[]

        libro = Libro(id2, titulo, genero, ISBN, editorial, autores)

        libronuevo.append(libro.get_id())
        libronuevo.append(libro.get_titulo())
        libronuevo.append(libro.get_genero())
        libronuevo.append(libro.get_ISBN())
        libronuevo.append(libro.get_editorial())
        libronuevo.append(libro.get_autores())
        data.append(libronuevo)
        data.sort()

    with open("Registros Libros.csv",'w', newline='') as ar:
        w=csv.writer(ar)
        w.writerows(data)

        #print(data)
        #next(reader)

    print("Se ha modificado el libro de ID " + id2 + " correctamente")

    repetir_opciones() 

def guardar_archivo():
    with open("Registros Libros.csv",'r') as ar:
        reader = csv.reader(ar)
        data=[line for line in reader]
        namefile=input('Digite el nombre del archivo a guardar (ejemplo: libros.txt o libros.csv''): ' )
    with open(namefile, 'w') as f:
        f.write("ID, Título, Género, ISBN, Editorial, Autor(es)\n")
        for list in data:
            f.write("\n")
            f.write(','.join(list))
            
    repetir_opciones() 

def run():

    print_options()
    command = input("Selecciona una opción:  ")

    if command == '1':
        f = open("Registros Libros.csv", "r")
        line= 4
        for x in range(line):
            a = f.readline()
            print(a)
        # with open("Registros Libros,csv","r") as archivo:
        #      for i in range(4):
        #          line = next(archivo).strip()
        #          print(line)
        repetir_opciones()         
    elif command == '2':
        listar_libros()
    elif command == '3':
        crear_registro_libro()
    elif command == '4':
        eliminar()
    elif command == '5':
        #buscar_libro_isbn()
        buscar_libroxisbn()
    elif command == '6':
        ordenar_libros()
        pass
    elif command == '7':
        pass
    elif command == '8':
        pass
    elif command == '9':
        actualizar_libro()
        #pass
    elif command == '10':
        guardar_archivo()
        #pass
    elif command == '11':
        os._exit(1)

    else:
        print('Opcion inválida, ingrese un numero del 1 al 10')
        time.sleep(2)
        run()

if __name__ == "__main__":
    run()
