from pip._vendor import requests
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
def menu():
    
    opciones=True
    while opciones:
        
        print(MAGENTA+"_________________LISTA DE OPCIONES A PEDIR ___________________\n")
        print(RED+"OPCION 1:-> LISTAR POKEMON POR GENERACION")
        print(BLUE+"OPCION 2:-> LISTAR POKEMON POR FORMA")
        print(CYAN+"OPCION 3:-> LISTAR POKEMONS POR HABILIDAD")
        print(WHITE+"OPCION 4:-> LISTAR POKEMON POR HABITAD")
        print(GREEN+"OPCION 5:-> LISTAR POKEMON POR TIPO")
        print(YELLOW+"OPCION 6:-> Salir")
        print("*************************************************\n")
        try:
            opcion=int(input("Digite una opción (número): "))
            if opcion==1:
                pass
            elif opcion==2:
                pass
            elif opcion==3:
                pass
            elif opcion==4:
                pass
            elif opcion==5:
                pass
            elif opcion==6:
                pass
            else:
                print("TIENE QUE INGRESAR UNA OPCION DE 1 AL 6")
        except Exception as excep:
            print("SE ENCONTRARON ERRORES", excep)
menu()