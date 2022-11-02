import csv

class ArchivosCSV:
    def _init__(self, schema, filename):
        self.__filename = f'./{filename}.csv'
        try:
            f = open(self.__filename)
            f.close()
        except IOError:
            with open(self.__filename, mode='w', encoding='utf-16') as csv_file:
                data_writer = csv.writer(csv_file, delimiter=';', quotechar='"',  quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
                data_writer.writerow(schema.keys())
    
    def insert(self, data):
        id_libro = self.get_last_id() + 1
        line = [id_libro] + data

        with open(self._filename, mode='a', encoding='utf-16') as csv_file:
            data_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            data_writer.writerow(line)
            
        return True

    def _get_last_id(self):
        list_ids = []
        with open(self.__filename, mode='r', encoding='utf-16') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            is_header = True
            for row in csv_reader:
                if is_header:
                    is_header = False
                    continue

                if row:
                    list_ids.append(row[0])
        if not list_ids:
            return 0 
            
        list_ids.sort(reverse = True)
        return int(list_ids[0])       