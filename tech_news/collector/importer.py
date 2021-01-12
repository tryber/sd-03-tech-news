import csv


def csv_importer(filepath):
    response = []
    try:
        if not filepath.endswith('.csv'):
            raise ValueError('Formato invalido')
        with open(filepath, 'r') as file:
            file_reader = csv.reader(file, delimiter=';')
            header, *data = file_reader
            for item in data:
                new_item = {}
                for i in range(len(header)):
                    new_item[header[i]] = item[i]
                response.append(new_item)
    except FileNotFoundError:
        raise ValueError("Arquivo file_not_exist.csv não encontrado")
    else:
        return response
