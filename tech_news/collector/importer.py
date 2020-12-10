import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    if not filepath.endswith('.csv'):
        raise ValueError('Formato invalido')
    try:
        with open(filepath) as file:
            test = csv.reader(file, delimiter=";", quotechar='"')
            header, *data = test
            print(header)
            print(data)
            return data
    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")


if __name__ == "__main__":
    csv_importer('tests/file_not_exist.csv')
