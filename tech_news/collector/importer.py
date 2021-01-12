import csv
from os import path


def csv_importer(filepath):
    result = []
    if not filepath.endswith('.csv'):
        raise ValueError('Formato invalido')
    if not path.exists(filepath):
        raise ValueError('Arquivo file_not_exist.csv não encontrado')

    with open(filepath, 'r') as file:
        file_reader = csv.reader(file, delimiter=';')
        header, *data = file_reader
        for item in data:
            new_item = {}
            for i in range(len(header)):
                new_item[header[i]] = item[i]
            result.append(new_item)
    return result
