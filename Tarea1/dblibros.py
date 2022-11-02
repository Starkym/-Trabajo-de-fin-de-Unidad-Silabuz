from .archivocsv import ArchivosCSV

SCHEMA = {
    'ID': {
        'type': 'autoincrement',
    }, 
    'TITULO': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    }, 
    'GENERO': {
        'type': 'string',
        'min_length': 5,
        'max_length': 100
    }, 
    'ISBN': {
        'type': 'int',
        'min_length': 15,
        'max_length': 25
    }, 
    'EDITORIAL': {
        'type': 'string',
        'min_length': 5,
        'max_length': 100
    }, 
    'AUTORES': {
        'type': 'string',
        'min_length': 5,
        'max_length': 200
    }
}

class DBLibros(ArchivosCSV):
    def __init__(self):
        super().__init__(SCHEMA, 'Libros')


    def save_libro(self, nuevolibro):
        data = [nuevolibro.titulo, nuevolibro.genero, nuevolibro.ISBN, nuevolibro.editorial, nuevolibro.autores]
        return self.insert(data)


    def update_libro(self):
        pass


    def delete_libro(self):
        pass

    def get_schema(self):
        return SCHEMA