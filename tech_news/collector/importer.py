import csv
from os import path


def csv_importer(filepath):
    exists = path.exists(filepath)
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    if not exists:
        raise ValueError("Arquivo file_not_exist.csv não encontrado")

    data = []
    with open(filepath) as file:
        csv_file = csv.DictReader(file, delimiter=";", quotechar='"')
        data = [item for item in csv_file]
    return data
