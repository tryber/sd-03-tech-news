import csv


def csv_importer(filepath):
    csv_data = []
    try:
        result = filepath.endswith("csv")

        if not result:
            raise ValueError("Formato invalido")
        with open(filepath) as file:
            beach_status_reader = csv.reader(file,
                                             delimiter=";", quotechar='"')
            header, *data = beach_status_reader
            dict = {}
            for row, index in enumerate(header):
                dict[index] = data[0][row]
        csv_data.append(dict)
        print(csv_data[0]["timestamp"])
        return csv_data
    except FileNotFoundError:
        raise ValueError("Arquivo file_not_exist.csv não encontrado")
