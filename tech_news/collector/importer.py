import csv
from os import path


def csv_importer(filepath):
    exists = path.exists(filepath)
    if not filepath.endswith('.csv'):
        return print('File não possui a extensão csv')
    if not exists:
        return print('Arquivo não existe')

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
