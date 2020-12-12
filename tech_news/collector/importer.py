import csv
from os import path


def csv_importer(filepath):
    """Seu código deve vir aqui"""
    exists = path.exists(filepath)
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    if not exists:
        raise ValueError("Arquivo file_not_exist.csv não encontrado")
    with open(filepath) as file:
        raw_csv = csv.DictReader(file, delimiter=";", quotechar='"')
        news = []
        for new in raw_csv:
            news.append(new)
        return news


if __name__ == "__main__":
    print(csv_importer('./correct.csv'))
