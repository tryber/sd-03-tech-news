import csv


def csv_importer(filepath):
    result = filepath.endswith("csv")
    print(result)
    if not result:
        raise ValueError("Formato invalido")
    with open(filepath) as file:
        beach_status_reader = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = beach_status_reader

        return header, data
