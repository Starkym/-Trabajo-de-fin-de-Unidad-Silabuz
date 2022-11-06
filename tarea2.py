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

class Pokemon:
    def __init__(self):
        self.__nombre=""
        self.__habilidades=""
        self.__url=[]
    
    def set_nombre(self,nombre):
        self.__nombre=nombre
    def set_atributos(self,habilidades):
        self.__habilidades=habilidades
    def set_atributos(self,url):
        self.__url=url
      
    def get_atributos(self):
        return self.__nombre, self.__habilidades,self.__url
    def get_nombre(self):
        return self.__nombre
    def get_habilidades(self):
        return self.__habilidades
    def get_url(self):
        return self.__url

    def print_name_hability_link(self):
        dato_pokemon=extract_json(f'https://pokeapi.co/api/v2/pokemon/{self.__nombre}')
        self.__habilidades = extract_habilidades(dato_pokemon)
        url_imagen= dato_pokemon['sprites']['other']
        self.__url=url_imagen['official-artwork']['front_default']
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
        print(f'Nombre del Pokémon: {self.__nombre}')
        print(f'Habilidades de {self.__nombre}: ',', '.join(self.__habilidades))
        print(f'URL de la imagen: ',self.__url)
        print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')  
    
   
class Pokemon2:
    def lista_por_generacion(self):
        pokemo=Pokemon()
        generation=int(input("QUE GENERACION DESEA VERIFICAR? INDIQUE VALOR DEL 1 AL 8 :"))
        data=extract_json(f"https://pokeapi.co/api/v2/generation/{generation}")
        pokemons_in_generation=[i['name'] for i in data['pokemon_species']]
        for j,poke1 in enumerate(pokemons_in_generation, start=1):
            pokemo.set_nombre(poke1)
            print(f'\n POKÉMON N° {j}')
            pokemo.print_name_hability_link()

def extract_json(url):
    json1=requests.get(url,stream=True)
    json1=json1.json()
    return json1   
def extract_habilidades(datos):
    return [elem['ability']['name'] for elem in datos['abilities']]



def menu():
    
    opciones=True
    while opciones:
        sistema=Pokemon2()
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
                sistema.lista_por_generacion()
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