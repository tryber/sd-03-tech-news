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


def csv_importer(filepath):
    news_summary = []
    if not Path(filepath).suffix == ".csv":
        raise ValueError("Extensão inválida")
    with open(filepath) as file:
        news = csv.reader(file, delimiter=";", quotechar='"')
        header, *data = news
        if header != HEADER:
            raise ValueError("Conteúdo inválido")
        for news in data:
            news_summary.append({
                header[0]: news[0],
                header[1]: news[1],
                header[2]: news[2],
                header[3]: news[3],
                header[4]: int(news[4]),
                header[5]: int(news[5]),
                header[6]: news[6],
                header[7]: news[7],
                header[8]: news[8]
                })
    return news_summary
