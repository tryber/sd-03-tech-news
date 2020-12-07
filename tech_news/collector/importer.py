import csv


def csv_importer(filepath):
    DICT = []
    if filepath.endswith('.json'):
        raise ValueError("Formato invalido")
    try:
        with open(filepath) as file:
            beach_status_reader = csv.reader(file, delimiter=";")
            header, *data = beach_status_reader
            dict = {}
            for row, index in enumerate(header):
                dict[index] = data[0][row]
        DICT.append(dict)
        return DICT
    except FileNotFoundError:
        raise ValueError("Arquivo file_not_exist.csv não encontrado")
