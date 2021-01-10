import csv


def csv_importer(filepath):
    try:
        if not filepath.endswith(".csv"):
            raise ValueError("Formato invalido")
        with open(filepath, "r") as file:
            content = csv.DictReader(file, delimiter=";")
            values = [value for value in content]
            return values
    except FileNotFoundError:
        raise ValueError("Arquivo file_not_exist.csv não encontrado")
