from os import path
import csv


def csv_importer(filepath):
    if path.splitext(filepath)[1] != '.csv':
        raise ValueError('Formato invalido')
    if path.exists(filepath) is False:
        raise ValueError(f"Arquivo {path.basename(filepath)} não encontrado")
    new_list = []
    with open(filepath) as file:
        reader = csv.reader(file, delimiter=";", quotechar='"')
        header, *data = reader
        for row in data:
            current = dict()
            for i in range(len(row)):
                current[header[i]] = row[i]
            new_list.append(current)
    return new_list
