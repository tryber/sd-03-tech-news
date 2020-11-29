import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    try:
        with open(filepath) as file:
            if not filepath.endswith('.csv'):
                raise ValueError()
            content = csv.DictReader(file, delimiter=';', )
            table = [value for value in content]
            return table
    except ValueError:
        file_name = filepath.split('/')[1]
        raise ValueError(
            f'Formato invalido : Arquivo {file_name} não encontrado')


# csv_importer('correct.csv')
