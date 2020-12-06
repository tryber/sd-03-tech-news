from pathlib import Path
import csv

HEADER = [
    'url',
    'title',
    'timestamp',
    'writer',
    'shares_count',
    'comments_count',
    'summary',
    'sources',
    'categories'
]


def check_path(filepath):
    if not Path(filepath).suffix == ".csv":
        raise ValueError("Formato invalido")
    return filepath.split("/")[-1]


def csv_importer(filepath):
    news_summary = []
    file = check_path(filepath)
    try:
        with open(filepath) as file:
            news = csv.reader(file, delimiter=";", quotechar='"')
            header, *data = news
            if header != HEADER:
                raise ValueError("Headers invalidos")
            # ref.:
            # https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
            for news in data:
                news_summary.append({
                    HEADER[i]: news[i] for i in range(len(HEADER))
                })
    except FileNotFoundError:
        raise ValueError(f"Arquivo {file} não encontrado")
    else:
        return news_summary
