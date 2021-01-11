import csv


def csv_importer(filepath):

    try:
        if not filepath.endswith(".csv"):
            raise ValueError("Formato invalido")
        with open(filepath) as file:
            csv_file = csv.DictReader(file, delimiter=";", quotechar='"')
            data = [item for item in csv_file]
            return data
    except FileNotFoundError:
        raise ValueError("Arquivo file_not_exist.csv não encontrado")
