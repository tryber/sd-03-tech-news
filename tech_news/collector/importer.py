import csv
from os import path


def csv_importer(filepath):
    exists = path.exists(filepath)
    if not filepath.endswith('.csv'):
        raise ValueError('Formato invalido')
    if not exists:
        raise ValueError('Arquivo file_not_exist.csv não encontrado')

    data_list = []
    with open(filepath) as file:
        readable = csv.reader(file, delimiter=";", quotechar='"')
        headers, *data = readable
        for list in data:
            dict = {}
            for index, header in enumerate(headers):
                dict[header] = list[index]
            data_list.append(dict)
    return data_list


print(csv_importer('correct.csv'))
